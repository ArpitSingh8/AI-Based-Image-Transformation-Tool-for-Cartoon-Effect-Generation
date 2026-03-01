import sys
import os
import streamlit as st
import cv2
import numpy as np
from PIL import Image

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from backend.database import create_users_table

# Page Configuration
st.set_page_config(
    page_title="CartoonifyAI - Transform Your Photos",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Database
create_users_table()

# Session State Initialization
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "user" not in st.session_state:
    st.session_state.user = None

# Professional CSS with Image Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main Container */
    .main {
        padding: 0;
    }
    
    /* Hero Section with Background */
    .hero-section {
        background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #4facfe);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        padding: 5rem 2rem;
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: rotate 20s linear infinite;
    }
    
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    .hero-title {
        color: white !important;
        font-size: 4rem;
        font-weight: 900;
        margin: 0;
        position: relative;
        z-index: 1;
        text-shadow: 0 4px 20px rgba(0,0,0,0.3);
        letter-spacing: -2px;
    }
    
    .hero-subtitle {
        color: rgba(255,255,255,0.95) !important;
        font-size: 1.5rem;
        margin-top: 1rem;
        position: relative;
        z-index: 1;
        font-weight: 400;
    }
    
    .hero-cta {
        margin-top: 2rem;
        position: relative;
        z-index: 1;
    }
    
    /* Section Container */
    .section-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 4rem 2rem;
    }
    
    .section-title {
        font-size: 2.5rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .section-subtitle {
        text-align: center;
        font-size: 1.2rem;
        opacity: 0.7;
        margin-bottom: 3rem;
    }
    
    /* Example Gallery */
    .example-gallery {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
    }
    
    .example-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        overflow: hidden;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
        position: relative;
    }
    
    .example-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.4);
        border-color: rgba(102, 126, 234, 0.6);
    }
    
    .example-image-container {
        position: relative;
        width: 100%;
        height: 250px;
        overflow: hidden;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .example-image {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.4s ease;
    }
    
    .example-card:hover .example-image {
        transform: scale(1.1);
    }
    
    .example-overlay {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(to top, rgba(0,0,0,0.8) 0%, transparent 60%);
        display: flex;
        align-items: flex-end;
        padding: 1.5rem;
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .example-card:hover .example-overlay {
        opacity: 1;
    }
    
    .example-badge {
        position: absolute;
        top: 1rem;
        right: 1rem;
        background: rgba(255, 255, 255, 0.9);
        color: #667eea;
        padding: 0.5rem 1rem;
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 700;
        z-index: 2;
    }
    
    .example-info {
        padding: 1.5rem;
        text-align: center;
    }
    
    .example-title {
        font-weight: 700;
        font-size: 1.2rem;
        margin-bottom: 0.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .example-desc {
        font-size: 0.95rem;
        opacity: 0.7;
        line-height: 1.6;
    }
    
    /* Feature Cards */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
    }
    
    .feature-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2rem;
        border-radius: 20px;
        transition: all 0.3s ease;
        text-align: center;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(102, 126, 234, 0.25);
        border-color: rgba(102, 126, 234, 0.5);
        background: rgba(102, 126, 234, 0.08);
    }
    
    .feature-icon {
        font-size: 3.5rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    .feature-title {
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 0.75rem;
    }
    
    .feature-desc {
        opacity: 0.8;
        line-height: 1.7;
        font-size: 1rem;
    }
    
    /* CTA Section */
    .cta-section {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border: 1px solid rgba(102, 126, 234, 0.3);
        padding: 4rem 2rem;
        border-radius: 24px;
        text-align: center;
        margin: 4rem 0;
    }
    
    .cta-title {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 1rem;
    }
    
    .cta-desc {
        font-size: 1.2rem;
        opacity: 0.8;
        margin-bottom: 2rem;
    }
    
    /* Comparison Slider */
    .comparison-container {
        position: relative;
        max-width: 800px;
        margin: 3rem auto;
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    }
    
    /* Stats Section */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
    }
    
    .stat-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border: 1px solid rgba(102, 126, 234, 0.3);
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        border-color: rgba(102, 126, 234, 0.6);
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        display: block;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-size: 1.1rem;
        opacity: 0.8;
        font-weight: 600;
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 1rem 3rem;
        font-weight: 700;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        letter-spacing: 0.5px;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(102, 126, 234, 0.6);
    }
</style>
""", unsafe_allow_html=True)

# Cartoonify Function (kept for compatibility)
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

# Hero Section
st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">🎨 CartoonifyAI</h1>
    <p class="hero-subtitle">Transform your photos into stunning cartoon artwork with AI-powered magic</p>
    <div class="hero-cta">
        <span style="background: rgba(255,255,255,0.2); backdrop-filter: blur(10px); padding: 0.75rem 2rem; 
                     border-radius: 50px; color: white; font-size: 1rem; font-weight: 600; 
                     border: 1px solid rgba(255,255,255,0.3);">
            ✨ 5 Artistic Styles | ⚡ Instant Processing | 📥 Free Download
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

# Authentication Check
if st.session_state.authenticated:
    # Redirect authenticated users to Dashboard
    st.switch_page("pages/Dashboard.py")

else:
    # Landing Page for Non-Authenticated Users
    
    # Example Gallery Section
    st.markdown("""
    <div class="section-container">
        <h2 class="section-title">See the Magic in Action</h2>
        <p class="section-subtitle">Explore different artistic styles and transformations</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Example Cards
    col1, col2, col3 = st.columns(3, gap="large")
    
    examples = [
        {
            "title": "Classic Cartoon",
            "desc": "Bold edges with smooth, vibrant colors",
            "icon": "🎨",
            "badge": "Most Popular"
        },
        {
            "title": "Pencil Sketch",
            "desc": "Detailed black and white artistic sketch",
            "icon": "✏️",
            "badge": "Artistic"
        },
        {
            "title": "Watercolor",
            "desc": "Soft, painted look with blended colors",
            "icon": "🖌️",
            "badge": "Premium"
        }
    ]
    
    for col, example in zip([col1, col2, col3], examples):
        with col:
            st.markdown(f"""
            <div class="example-card">
                <div class="example-image-container">
                    <div class="example-badge">{example['badge']}</div>
                    <div style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-size: 5rem;">
                        {example['icon']}
                    </div>
                    <div class="example-overlay">
                        <p style="color: white; margin: 0; font-weight: 600;">Click to see examples</p>
                    </div>
                </div>
                <div class="example-info">
                    <h3 class="example-title">{example['title']}</h3>
                    <p class="example-desc">{example['desc']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Stats Section
    st.markdown("""
    <div class="section-container">
        <div class="stats-grid">
            <div class="stat-card">
                <span class="stat-number">10K+</span>
                <span class="stat-label">Images Transformed</span>
            </div>
            <div class="stat-card">
                <span class="stat-number">5</span>
                <span class="stat-label">Artistic Styles</span>
            </div>
            <div class="stat-card">
                <span class="stat-number">< 3s</span>
                <span class="stat-label">Processing Time</span>
            </div>
            <div class="stat-card">
                <span class="stat-number">100%</span>
                <span class="stat-label">Free to Use</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Features Section
    st.markdown("""
    <div class="section-container">
        <h2 class="section-title">Why Choose CartoonifyAI?</h2>
        <p class="section-subtitle">Professional-grade image transformation at your fingertips</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature Grid
    features = [
        ("🎨", "AI-Powered Magic", "Advanced computer vision algorithms transform your photos with professional quality"),
        ("⚙️", "Full Customization", "Fine-tune parameters for each style to match your creative vision"),
        ("📥", "Instant Downloads", "Export your artwork in high-quality PNG format, ready for any use"),
        ("🔒", "Privacy First", "Your images are processed securely and never stored on our servers"),
        ("⚡", "Lightning Fast", "Get results in seconds with our optimized processing pipeline"),
        ("🎯", "Perfect Results", "Consistently stunning output across all image types and sizes")
    ]
    
    col1, col2, col3 = st.columns(3, gap="large")
    cols = [col1, col2, col3]
    
    for idx, (icon, title, desc) in enumerate(features):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="feature-card">
                <span class="feature-icon">{icon}</span>
                <h3 class="feature-title">{title}</h3>
                <p class="feature-desc">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # CTA Section
    st.markdown("""
    <div class="section-container">
        <div class="cta-section">
            <h2 class="cta-title">Ready to Transform Your Photos?</h2>
            <p class="cta-desc">Join thousands of users creating stunning cartoon artwork</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        col_a, col_b = st.columns(2, gap="medium")
        with col_a:
            if st.button("🚀 Get Started Free", width="stretch", type="primary"):
                st.switch_page("pages/Register.py")
        with col_b:
            if st.button("🔐 Login", width="stretch"):
                st.switch_page("pages/Login.py")
    
    st.markdown("<br><br>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; opacity: 0.6; padding: 2rem;">
    <p style="font-size: 1rem; margin-bottom: 0.5rem;">Made with ❤️ using Streamlit & OpenCV | © 2026 CartoonifyAI</p>
    <p style="font-size: 0.9rem; opacity: 0.8;">Transforming memories into art, one pixel at a time</p>
</div>
""", unsafe_allow_html=True)
