import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
</style>
""", unsafe_allow_html=True)

# Cartoonify Function
def cartoonify_image(image, edge_strength=9, color_smoothing=9):
    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray_blur = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(
        gray_blur, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        edge_strength, 9
    )
    color = cv2.bilateralFilter(img, color_smoothing, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

# Header
st.markdown("""
<div class="page-header">
    <h1 class="page-title">🎨 Image Transformation Studio</h1>
    <p class="page-subtitle">Upload your photo and watch the AI magic happen</p>
</div>
""", unsafe_allow_html=True)

# Navigation
col1, col2, col3 = st.columns([1, 4, 1])
with col1:
    if st.button("← Back to Dashboard", width="stretch"):
        st.switch_page("pages/Dashboard.py")

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
    
    # Advanced Settings
    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("🎛️ Advanced Controls", expanded=False):
        st.markdown("Fine-tune the transformation to match your creative vision")
        col1, col2 = st.columns(2)
        with col1:
            edge_strength = st.slider(
                "Edge Definition", 
                5, 15, 9, 2, 
                help="Higher values create stronger, more defined outlines"
            )
        with col2:
            color_smoothing = st.slider(
                "Color Smoothness", 
                5, 15, 9, 2, 
                help="Higher values create smoother, more uniform colors"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Image Display
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
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
    
    with col2:
        st.markdown('<div class="image-label">✨ Cartoonified Result</div>', unsafe_allow_html=True)
        
        with st.spinner("🎨 Transforming your image... This may take a moment"):
            cartoon_image = cartoonify_image(image, edge_strength, color_smoothing)
        
        st.image(cartoon_image, width="stretch")
        
        # Success Message
        st.success("✅ Transformation complete!")
    
    # Download Section
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown('<p style="font-size: 1.3rem; font-weight: 700; margin-bottom: 1rem; text-align: center;">💾 Download Your Artwork</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        result = Image.fromarray(cartoon_image)
        buf = BytesIO()
        result.save(buf, format="PNG")
        byte_im = buf.getvalue()
        
        st.download_button(
            label="📥 Download Cartoon Image",
            data=byte_im,
            file_name=f"cartoonify_{uploaded_file.name.split('.')[0]}.png",
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
            Supported formats: JPG, JPEG, PNG
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tips
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<p style="font-size: 1.3rem; font-weight: 700; margin-bottom: 1.5rem;">💡 Tips for Best Results</p>', unsafe_allow_html=True)
    
    tip_col1, tip_col2, tip_col3 = st.columns(3, gap="medium")
    
    tips = [
        ("📸", "High Quality", "Use clear, well-lit photos for the best cartoon effects"),
        ("🎨", "Experiment", "Try different settings to find your perfect style"),
        ("🖼️", "Portraits", "Portrait photos work especially well with our AI")
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
    <p style="font-size: 0.9rem;">© 2024 CartoonifyAI | Transforming memories into art</p>
</div>
""", unsafe_allow_html=True)
