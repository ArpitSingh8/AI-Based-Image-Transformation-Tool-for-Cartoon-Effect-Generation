import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Page Configuration
st.set_page_config(
    page_title="Dashboard - CartoonifyAI",
    page_icon="📊",
    layout="wide"
)

# Route Protection
if not st.session_state.get("authenticated", False):
    st.warning("⚠️ Please login to access the dashboard")
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
    
    /* Hero Section */
    .dashboard-hero {
        background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #4facfe);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        padding: 3rem 2rem;
        border-radius: 24px;
        margin-bottom: 2rem;
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.3);
        text-align: center;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .hero-welcome {
        color: white !important;
        font-size: 3rem;
        font-weight: 800;
        margin: 0;
        text-shadow: 0 4px 20px rgba(0,0,0,0.2);
    }
    
    .hero-subtitle {
        color: rgba(255,255,255,0.95) !important;
        font-size: 1.2rem;
        margin-top: 0.5rem;
    }
    
    /* Glass Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(102, 126, 234, 0.2);
        border-color: rgba(102, 126, 234, 0.3);
    }
    
    .card-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    .card-title {
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .card-desc {
        opacity: 0.8;
        line-height: 1.6;
        margin-bottom: 1.5rem;
    }
    
    /* Stats Card */
    .stat-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border: 1px solid rgba(102, 126, 234, 0.3);
        padding: 1.5rem;
        border-radius: 16px;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        border-color: rgba(102, 126, 234, 0.6);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .stat-label {
        opacity: 0.7;
        font-size: 0.95rem;
        margin-top: 0.5rem;
    }
    
    /* Info Box */
    .info-box {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 1rem 1.5rem;
        border-radius: 12px;
        margin: 0.5rem 0;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .info-label {
        opacity: 0.7;
        font-size: 0.9rem;
    }
    
    .info-value {
        font-weight: 600;
        font-size: 1.05rem;
    }
    
    /* Button Styling */
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
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
user_name = st.session_state.user[1] if st.session_state.user else "User"
st.markdown(f"""
<div class="dashboard-hero">
    <h1 class="hero-welcome">Welcome back, {user_name}! 👋</h1>
    <p class="hero-subtitle">Ready to transform your photos into stunning cartoon artwork?</p>
</div>
""", unsafe_allow_html=True)

# Main Dashboard Content
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    # Quick Actions
    st.markdown('<p style="font-size: 1.5rem; font-weight: 700; margin-bottom: 1.5rem;">Quick Actions</p>', unsafe_allow_html=True)
    
    action_col1, action_col2 = st.columns(2, gap="medium")
    
    with action_col1:
        st.markdown("""
        <div class="glass-card">
            <span class="card-icon">🎨</span>
            <h3 class="card-title">Transform Image</h3>
            <p class="card-desc">Upload and convert your photos into beautiful cartoon artwork with AI</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🚀 Start Transforming", key="transform_btn", width="stretch"):
            st.switch_page("pages/Transform.py")
    
    with action_col2:
        st.markdown("""
        <div class="glass-card">
            <span class="card-icon">⚙️</span>
            <h3 class="card-title">Settings</h3>
            <p class="card-desc">Manage your account settings, preferences, and security options</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔧 Manage Settings", key="settings_btn", width="stretch"):
            st.info("Settings page coming soon!")
    
    # Recent Activity
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p style="font-size: 1.5rem; font-weight: 700; margin-bottom: 1.5rem;">Your Stats</p>', unsafe_allow_html=True)
    
    stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
    
    stats = [
        ("🎨", "0", "Transforms"),
        ("📥", "0", "Downloads"),
        ("⭐", "Pro", "Account"),
        ("🔥", "0", "Streak")
    ]
    
    for col, (icon, number, label) in zip([stat_col1, stat_col2, stat_col3, stat_col4], stats):
        with col:
            st.markdown(f"""
            <div class="stat-card">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">{icon}</div>
                <div class="stat-number">{number}</div>
                <div class="stat-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)

with col2:
    # Account Information
    st.markdown('<p style="font-size: 1.5rem; font-weight: 700; margin-bottom: 1.5rem;">Account Details</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="glass-card">
        <span class="card-icon">👤</span>
        <h3 class="card-title">Profile Information</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # User Details
    user_data = st.session_state.user
    st.markdown(f"""
    <div class="info-box">
        <span class="info-label">Username</span>
        <span class="info-value">{user_data[1]}</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="info-box">
        <span class="info-label">Email</span>
        <span class="info-value">{user_data[2]}</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="info-box">
        <span class="info-label">Account Type</span>
        <span class="info-value">Free</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="info-box">
        <span class="info-label">Member Since</span>
        <span class="info-value">Today</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Logout Button
    if st.button("🔓 Logout", key="logout_btn", width="stretch"):
        st.session_state.authenticated = False
        st.session_state.user = None
        st.success("✅ Logged out successfully!")
        st.info("👉 Redirecting to login page...")
        st.rerun()

# Tips Section
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<p style="font-size: 1.5rem; font-weight: 700; margin-bottom: 1.5rem;">💡 Pro Tips</p>', unsafe_allow_html=True)

tip_col1, tip_col2, tip_col3 = st.columns(3, gap="medium")

tips = [
    ("📸", "Best Results", "Use high-quality images with good lighting for the best cartoon effects"),
    ("🎛️", "Experiment", "Try different edge strength and color smoothing settings for unique styles"),
    ("💾", "Save Often", "Download your favorite transformations to build your cartoon collection")
]

for col, (icon, title, desc) in zip([tip_col1, tip_col2, tip_col3], tips):
    with col:
        st.markdown(f"""
        <div class="glass-card" style="text-align: center;">
            <span class="card-icon">{icon}</span>
            <h4 style="font-weight: 700; margin-bottom: 0.5rem;">{title}</h4>
            <p style="opacity: 0.8; font-size: 0.9rem; line-height: 1.6;">{desc}</p>
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
