import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.image_processor import ImageProcessor

# Page Configuration
st.set_page_config(
    page_title="Transform - CartoonifyAI",
    page_icon="🎨",
    layout="wide"
)

# Route Protection
if not st.session_state.get("authenticated", False):
    st.warning("⚠️ Please login to access the image transformation tool")
    st.info("👉 Redirecting to login page...")
    st.switch_page("pages/Login.py")
    st.stop()

# Modern CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Header */
    .page-header {
        background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #4facfe);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.3);
        text-align: center;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .page-title {
        color: white !important;
        font-size: 2.5rem;
        font-weight: 800;
        margin: 0;
        text-shadow: 0 4px 20px rgba(0,0,0,0.2);
    }
    
    .page-subtitle {
        color: rgba(255,255,255,0.95) !important;
        font-size: 1.1rem;
        margin-top: 0.5rem;
    }
    
    /* Style Cards */
    .style-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 2px solid rgba(255, 255, 255, 0.1);
        padding: 1.5rem;
        border-radius: 16px;
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
        height: 100%;
    }
    
    .style-card:hover {
        transform: translateY(-5px);
        border-color: rgba(102, 126, 234, 0.6);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
    }
    
    .style-card.selected {
        border-color: #667eea;
        background: rgba(102, 126, 234, 0.1);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    
    .style-icon {
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }
    
    .style-name {
        font-size: 1.2rem;
        font-weight: 700;
        margin: 0.5rem 0;
    }
    
    .style-desc {
        font-size: 0.9rem;
        opacity: 0.8;
        line-height: 1.4;
    }
    
    /* Glass Card */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    
    /* Image Label */
    .image-label {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 1.1rem;
        margin-bottom: 1rem;
        display: inline-block;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    /* File Uploader */
    [data-testid="stFileUploader"] {
        background: rgba(255, 255, 255, 0.03);
        border: 2px dashed rgba(102, 126, 234, 0.3);
        border-radius: 16px;
        padding: 2rem;
        transition: all 0.3s ease;
    }
    
    [data-testid="stFileUploader"]:hover {
        border-color: rgba(102, 126, 234, 0.6);
        background: rgba(102, 126, 234, 0.05);
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5);
    }
    
    .stDownloadButton > button {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(17, 153, 142, 0.3);
    }
    
    .stDownloadButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(17, 153, 142, 0.5);
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 12px;
        font-weight: 600;
    }
    
    /* Radio Buttons */
    .stRadio > div {
        background: rgba(255, 255, 255, 0.03);
        padding: 1rem;
        border-radius: 12px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for style selection
if 'selected_style' not in st.session_state:
    st.session_state.selected_style = 'classic'

# Header
st.markdown("""
<div class="page-header">
    <h1 class="page-title">🎨 Image Transformation Studio</h1>
    <p class="page-subtitle">Choose your style and watch the AI magic happen</p>
</div>
""", unsafe_allow_html=True)

# Navigation
col1, col2, col3 = st.columns([1, 4, 1])
with col1:
    if st.button("← Back to Dashboard", width="stretch"):
        st.switch_page("pages/Dashboard.py")

st.markdown("<br>", unsafe_allow_html=True)

# Style Selection
st.markdown('<p style="font-size: 1.3rem; font-weight: 700; margin-bottom: 1rem;">🎭 Choose Your Art Style</p>', unsafe_allow_html=True)

styles_info = ImageProcessor.get_style_info()

# Create style selection cards
style_cols = st.columns(5)
for idx, (style_key, style_data) in enumerate(styles_info.items()):
    with style_cols[idx]:
        selected_class = "selected" if st.session_state.selected_style == style_key else ""
        st.markdown(f"""
        <div class="style-card {selected_class}">
            <div class="style-icon">{style_data['icon']}</div>
            <div class="style-name">{style_data['name']}</div>
            <div class="style-desc">{style_data['description']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"Select", key=f"btn_{style_key}", width="stretch"):
            st.session_state.selected_style = style_key
            st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# Upload Section
st.markdown('<p style="font-size: 1.3rem; font-weight: 700; margin-bottom: 1rem;">📤 Upload Your Image</p>', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Drag and drop or click to browse",
    type=["jpg", "jpeg", "png"],
    help="Supported formats: JPG, JPEG, PNG (Max 200MB)",
    label_visibility="collapsed"
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    # Advanced Settings based on selected style
    st.markdown("<br>", unsafe_allow_html=True)
    current_style_info = styles_info[st.session_state.selected_style]
    
    with st.expander(f"🎛️ {current_style_info['name']} Settings", expanded=False):
        st.markdown("Fine-tune the transformation parameters")
        
        params = {}
        
        if st.session_state.selected_style == "classic":
            col1, col2, col3 = st.columns(3)
            with col1:
                params['edge_strength'] = st.slider(
                    "Edge Strength", 
                    5, 15, 9, 2,
                    help="Higher values = stronger outlines"
                )
            with col2:
                params['color_smoothing'] = st.slider(
                    "Color Smoothness", 
                    5, 15, 9, 2,
                    help="Higher values = smoother colors"
                )
            with col3:
                params['color_levels'] = st.slider(
                    "Color Levels", 
                    5, 15, 9, 2,
                    help="Number of color levels"
                )
        
        elif st.session_state.selected_style == "sketch":
            col1, col2 = st.columns(2)
            with col1:
                params['blur_value'] = st.slider(
                    "Blur Intensity", 
                    11, 31, 21, 2,
                    help="Higher values = softer sketch"
                )
            with col2:
                params['sigma_s'] = st.slider(
                    "Spatial Sigma", 
                    30, 100, 60, 10,
                    help="Controls detail level"
                )
        
        elif st.session_state.selected_style == "pencil":
            col1, col2 = st.columns(2)
            with col1:
                params['sigma_s'] = st.slider(
                    "Spatial Sigma", 
                    30, 100, 60, 10,
                    help="Controls detail level"
                )
            with col2:
                params['shade_factor'] = st.slider(
                    "Shade Factor", 
                    0.01, 0.1, 0.02, 0.01,
                    help="Controls shading intensity"
                )
        
        elif st.session_state.selected_style == "watercolor":
            col1, col2 = st.columns(2)
            with col1:
                params['blur_value'] = st.slider(
                    "Blur Intensity", 
                    9, 25, 15, 2,
                    help="Higher values = softer look"
                )
            with col2:
                params['edge_strength'] = st.slider(
                    "Edge Strength", 
                    5, 15, 7, 2,
                    help="Controls edge visibility"
                )
        
        elif st.session_state.selected_style == "oil":
            col1, col2 = st.columns(2)
            with col1:
                params['size'] = st.slider(
                    "Brush Size", 
                    3, 15, 7, 2,
                    help="Size of brush strokes"
                )
            with col2:
                params['dynRatio'] = st.slider(
                    "Dynamic Ratio", 
                    1, 3, 1, 1,
                    help="Controls color variation"
                )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Process Image Button
    col1, col2, col3 = st.columns([2, 2, 2])
    with col2:
        process_button = st.button("✨ Transform Image", width="stretch", type="primary")
    
    if process_button or 'processed_image' in st.session_state:
        # Image Display
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Create tabs for different views
        tab1, tab2, tab3 = st.tabs(["🔄 Side-by-Side", "📷 Original", "🎨 Transformed"])
        
        with st.spinner(f"🎨 Creating your {current_style_info['name']} masterpiece..."):
            try:
                # Process the image
                processed_image = ImageProcessor.process_image(
                    image,
                    style=st.session_state.selected_style,
                    **params
                )
                st.session_state.processed_image = processed_image
                
                # Create comparison
                comparison = ImageProcessor.create_comparison(image, processed_image)
                st.session_state.comparison = comparison
                
            except Exception as e:
                st.error(f"❌ Error processing image: {str(e)}")
                st.stop()
        
        with tab1:
            st.markdown('<div class="image-label">🔄 Before & After Comparison</div>', unsafe_allow_html=True)
            st.image(st.session_state.comparison, width="stretch", caption="Left: Original | Right: Transformed")
        
        with tab2:
            st.markdown('<div class="image-label">📷 Original Image</div>', unsafe_allow_html=True)
            st.image(image, width="stretch")
            
            # Image Info
            st.markdown(f"""
            <div style="background: rgba(255, 255, 255, 0.03); padding: 1rem; border-radius: 12px; margin-top: 1rem;">
                <p style="margin: 0; opacity: 0.7; font-size: 0.9rem;">
                    <strong>Filename:</strong> {uploaded_file.name}<br>
                    <strong>Size:</strong> {image.size[0]} x {image.size[1]} pixels<br>
                    <strong>Format:</strong> {image.format}
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        with tab3:
            st.markdown(f'<div class="image-label">✨ {current_style_info["name"]} Result</div>', unsafe_allow_html=True)
            st.image(st.session_state.processed_image, width="stretch")
            st.success(f"✅ {current_style_info['name']} transformation complete!")
        
        # Download Section
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown('<p style="font-size: 1.3rem; font-weight: 700; margin-bottom: 1rem; text-align: center;">💾 Download Your Artwork</p>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            # Convert to PIL Image for download
            result = Image.fromarray(st.session_state.processed_image)
            buf = BytesIO()
            result.save(buf, format="PNG")
            byte_im = buf.getvalue()
            
            st.download_button(
                label=f"📥 Download {current_style_info['name']}",
                data=byte_im,
                file_name=f"{current_style_info['name'].lower().replace(' ', '_')}_{uploaded_file.name.split('.')[0]}.png",
                mime="image/png",
                width="stretch"
            )
            
            st.markdown("""
            <div style="text-align: center; margin-top: 1rem; opacity: 0.7; font-size: 0.9rem;">
                <p>Your image will be downloaded as a high-quality PNG file</p>
            </div>
            """, unsafe_allow_html=True)

else:
    # Empty State
    st.markdown("""
    <div class="glass-card" style="text-align: center; padding: 4rem 2rem; margin-top: 2rem;">
        <div style="font-size: 5rem; margin-bottom: 1rem;">🖼️</div>
        <h3 style="margin: 1rem 0; font-size: 1.8rem;">No Image Uploaded Yet</h3>
        <p style="opacity: 0.7; font-size: 1.1rem; line-height: 1.8;">
            Upload an image above to start the transformation process.<br>
            Choose from 5 different artistic styles!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tips
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<p style="font-size: 1.3rem; font-weight: 700; margin-bottom: 1.5rem;">💡 Tips for Best Results</p>', unsafe_allow_html=True)
    
    tip_col1, tip_col2, tip_col3 = st.columns(3, gap="medium")
    
    tips = [
        ("📸", "High Quality", "Use clear, well-lit photos for the best results"),
        ("🎨", "Try All Styles", "Each style works differently - experiment to find your favorite"),
        ("🖼️", "Portraits Work Best", "Portrait and landscape photos produce stunning results")
    ]
    
    for col, (icon, title, desc) in zip([tip_col1, tip_col2, tip_col3], tips):
        with col:
            st.markdown(f"""
            <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1);
                        padding: 1.5rem; border-radius: 16px; text-align: center;">
                <div style="font-size: 2.5rem; margin-bottom: 1rem;">{icon}</div>
                <h4 style="font-weight: 700; margin-bottom: 0.5rem;">{title}</h4>
                <p style="opacity: 0.8; font-size: 0.9rem; line-height: 1.6; margin: 0;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
<div style="text-align: center; opacity: 0.6; padding: 1rem;">
    <p style="font-size: 0.9rem;">© 2026 CartoonifyAI | Transforming memories into art</p>
</div>
""", unsafe_allow_html=True)
