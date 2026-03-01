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

# Modern Glassmorphism CSS with Trending Design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main Container */
    .main {
        padding: 1rem 2rem;
    }
    
    /* Animated Gradient Header */
    .hero-container {
        background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #4facfe);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        padding: 3rem 2rem;
        border-radius: 24px;
        margin-bottom: 2rem;
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .hero-container::before {
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
        font-size: 3.5rem;
        font-weight: 800;
        margin: 0;
        text-align: center;
        position: relative;
        z-index: 1;
        text-shadow: 0 4px 20px rgba(0,0,0,0.2);
        letter-spacing: -1px;
    }
    
    .hero-subtitle {
        color: rgba(255,255,255,0.95) !important;
        font-size: 1.3rem;
        text-align: center;
        margin-top: 1rem;
        position: relative;
        z-index: 1;
        font-weight: 400;
    }
    
    .hero-badge {
        display: inline-block;
        background: rgba(255,255,255,0.2);
        backdrop-filter: blur(10px);
        padding: 0.5rem 1.5rem;
        border-radius: 50px;
        color: white;
        font-size: 0.9rem;
        font-weight: 600;
        margin-top: 1rem;
        border: 1px solid rgba(255,255,255,0.3);
    }
    
    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .glass-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
        transition: left 0.5s;
    }
    
    .glass-card:hover::before {
        left: 100%;
    }
    
    .glass-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 16px 48px rgba(102, 126, 234, 0.2);
        border-color: rgba(102, 126, 234, 0.4);
    }
    
    /* Feature Cards with Icons */
    .feature-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 1.8rem;
        border-radius: 16px;
        margin: 1rem 0;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .feature-card:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 12px 40px rgba(102, 126, 234, 0.25);
        border-color: rgba(102, 126, 234, 0.5);
        background: rgba(102, 126, 234, 0.08);
    }
    
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    .feature-title {
        font-size: 1.2rem;
        font-weight: 700;
        margin: 0.5rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .feature-desc {
        opacity: 0.8;
        font-size: 0.95rem;
        line-height: 1.6;
        margin: 0;
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

# Hero Section
st.markdown("""
<div class="hero-container">
    <h1 class="hero-title">🎨 CartoonifyAI</h1>
    <p class="hero-subtitle">Transform your photos into stunning cartoon artwork with AI-powered magic</p>
    <div style="text-align: center;">
        <span class="hero-badge">✨ Powered by Advanced Computer Vision</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Authentication Check
if st.session_state.authenticated:
    # Redirect authenticated users to Dashboard
    st.switch_page("pages/Dashboard.py")

else:
    # Landing Page for Non-Authenticated Users
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        st.markdown("""
        <div class="glass-card" style="text-align: center; padding: 3rem 2rem;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">🔐</div>
            <h2 style="margin-bottom: 1rem;">Get Started with CartoonifyAI</h2>
            <p style="opacity: 0.8; font-size: 1.1rem; line-height: 1.8;">
                Join thousands of users transforming their photos into stunning cartoon artwork. 
                Login or create a free account to unlock the magic!
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Features Grid
        st.markdown('<p style="font-size: 1.5rem; font-weight: 700; text-align: center; margin: 2rem 0;">Why Choose CartoonifyAI?</p>', unsafe_allow_html=True)
        
        features = [
            ("🎨", "AI-Powered Magic", "Advanced computer vision algorithms transform your photos with professional quality"),
            ("⚙️", "Full Customization", "Fine-tune edge strength and color smoothing to match your creative vision"),
            ("📥", "Instant Downloads", "Export your artwork in high-quality PNG format, ready for any use"),
            ("🔒", "Privacy First", "Your images are processed securely and never stored on our servers"),
            ("⚡", "Lightning Fast", "Get results in seconds with our optimized processing pipeline"),
            ("🎯", "Perfect Results", "Consistently stunning output that looks hand-drawn by professional artists")
        ]
        
        for i in range(0, len(features), 2):
            col_a, col_b = st.columns(2, gap="medium")
            
            with col_a:
                icon, title, desc = features[i]
                st.markdown(f"""
                <div class="feature-card">
                    <span class="feature-icon">{icon}</span>
                    <h3 class="feature-title">{title}</h3>
                    <p class="feature-desc">{desc}</p>
                </div>
                """, unsafe_allow_html=True)
            
            if i + 1 < len(features):
                with col_b:
                    icon, title, desc = features[i + 1]
                    st.markdown(f"""
                    <div class="feature-card">
                        <span class="feature-icon">{icon}</span>
                        <h3 class="feature-title">{title}</h3>
                        <p class="feature-desc">{desc}</p>
                    </div>
                    """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.info("👈 Use the sidebar to Login or Register and start creating!")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
<div style="text-align: center; opacity: 0.6; padding: 1.5rem;">
    <p style="font-size: 0.95rem;">Made with ❤️ using Streamlit & OpenCV | © 2026 CartoonifyAI</p>
    <p style="font-size: 0.85rem; margin-top: 0.5rem;">Transforming memories into art, one pixel at a time</p>
</div>
""", unsafe_allow_html=True)
