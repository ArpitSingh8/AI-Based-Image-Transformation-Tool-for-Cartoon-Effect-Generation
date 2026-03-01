import streamlit as st
from backend.auth import login_user

# Page Configuration
st.set_page_config(
    page_title="Login - CartoonifyAI",
    page_icon="🔐",
    layout="centered"
)

# Modern Theme-Adaptive CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Animated Background */
    .stApp {
        background: linear-gradient(-45deg, rgba(102, 126, 234, 0.05), rgba(118, 75, 162, 0.05), rgba(240, 147, 251, 0.05), rgba(79, 172, 254, 0.05));
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Header Styling */
    .login-header {
        text-align: center;
        margin-bottom: 2.5rem;
    }
    
    .login-icon {
        font-size: 5rem;
        margin-bottom: 1rem;
        display: block;
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .login-title {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -1px;
    }
    
    .login-subtitle {
        opacity: 0.7;
        font-size: 1.1rem;
        font-weight: 400;
    }
    
    /* Glass Card Container */
    .glass-container {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 3rem 2.5rem;
        border-radius: 24px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        max-width: 480px;
        margin: 2rem auto;
    }
    
    /* Input Styling */
    .stTextInput > div > div > input {
        border-radius: 12px;
        padding: 0.85rem 1rem;
        border: 2px solid rgba(128, 128, 128, 0.15);
        transition: all 0.3s ease;
        font-size: 1rem;
        background: rgba(255, 255, 255, 0.03);
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1);
        background: rgba(255, 255, 255, 0.05);
    }
    
    .stTextInput > label {
        font-weight: 600;
        font-size: 0.95rem;
        margin-bottom: 0.5rem;
    }
    
    /* Button Styling */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.85rem 2rem;
        font-size: 1.05rem;
        font-weight: 700;
        transition: all 0.3s ease;
        margin-top: 1.5rem;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        letter-spacing: 0.5px;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5);
    }
    
    /* Checkbox Styling */
    .stCheckbox {
        margin: 1rem 0;
    }
    
    /* Divider */
    .divider {
        text-align: center;
        margin: 2rem 0;
        position: relative;
        opacity: 0.5;
    }
    
    .divider::before,
    .divider::after {
        content: "";
        position: absolute;
        top: 50%;
        width: 42%;
        height: 1px;
        background: currentColor;
    }
    
    .divider::before { left: 0; }
    .divider::after { right: 0; }
    
    /* Info Box */
    .info-box {
        padding: 1.2rem;
        border-radius: 12px;
        border-left: 4px solid #667eea;
        background: rgba(102, 126, 234, 0.08);
        margin: 1.5rem 0;
        font-size: 0.95rem;
    }
    
    /* Register Link */
    .register-link {
        text-align: center;
        margin-top: 2rem;
        padding: 1.2rem;
        border-radius: 12px;
        background: rgba(128, 128, 128, 0.03);
        border: 1px solid rgba(128, 128, 128, 0.1);
    }
    
    /* Alert Styling */
    .stAlert {
        border-radius: 12px;
        border: none;
    }
</style>
""", unsafe_allow_html=True)

# Main Content
st.markdown("""
<div class="login-header">
    <span class="login-icon">🔐</span>
    <h1 class="login-title">Welcome Back</h1>
    <p class="login-subtitle">Login to CartoonifyAI and continue creating magic</p>
</div>
""", unsafe_allow_html=True)

# Login Form
with st.container():
    email = st.text_input(
        "Email Address",
        placeholder="your.email@example.com",
        key="login_email",
        help="Enter the email you registered with"
    )
    
    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password",
        key="login_password",
        help="Your password is encrypted and secure"
    )
    
    # Remember me and forgot password row
    col1, col2 = st.columns([1, 1])
    with col1:
        remember = st.checkbox("Remember me", value=True)
    with col2:
        st.markdown('<p style="text-align: right; opacity: 0.6; font-size: 0.9rem; margin-top: 0.5rem; cursor: pointer;">Forgot password?</p>', unsafe_allow_html=True)
    
    # Login Button
    if st.button("🚀 Login to CartoonifyAI", width="stretch"):
        if not email or not password:
            st.error("⚠️ Please fill in all fields")
        else:
            with st.spinner("🔄 Authenticating..."):
                success, result = login_user(email, password)
                
                if success:
                    st.session_state.authenticated = True
                    st.session_state.user = result
                    st.success("✅ Login successful! Redirecting to your dashboard...")
                    st.balloons()
                    st.switch_page("pages/Dashboard.py")
                else:
                    st.error(f"❌ {result}")

# Divider
st.markdown('<div class="divider"><span style="padding: 0 1rem; background: var(--background-color);">OR</span></div>', unsafe_allow_html=True)

# Register Link
st.markdown("""
<div class="register-link">
    <p style="margin: 0; opacity: 0.8; font-size: 1rem;">Don't have an account yet?</p>
    <p style="margin: 0.5rem 0 0 0; opacity: 0.6; font-size: 0.9rem;">Join CartoonifyAI and start transforming your photos</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("📝 Create Free Account", width="stretch"):
        st.switch_page("pages/Register.py")

# Footer Info
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div class="info-box">
    <p style="margin: 0; font-size: 0.95rem; line-height: 1.6;">
        🔒 <strong>Your security matters.</strong> All data is encrypted and we never share your information with third parties.
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; opacity: 0.5; font-size: 0.85rem;">
    <p>© 2026 CartoonifyAI | Transforming memories into art</p>
</div>
""", unsafe_allow_html=True)
