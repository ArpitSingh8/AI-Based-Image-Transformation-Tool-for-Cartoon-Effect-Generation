import streamlit as st
from backend.auth import register_user
from utils.validators import is_valid_email, is_strong_password

# Page Configuration
st.set_page_config(
    page_title="Register - CartoonifyAI",
    page_icon="📝",
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
    .register-header {
        text-align: center;
        margin-bottom: 2.5rem;
    }
    
    .register-icon {
        font-size: 5rem;
        margin-bottom: 1rem;
        display: block;
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .register-title {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -1px;
    }
    
    .register-subtitle {
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
    
    /* Password Strength Indicator */
    .password-strength {
        margin-top: 0.75rem;
        padding: 0.75rem 1rem;
        border-radius: 10px;
        font-size: 0.9rem;
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .strength-weak {
        background: rgba(255, 77, 77, 0.1);
        color: #ff4d4d;
        border-left: 4px solid #ff4d4d;
    }
    
    .strength-medium {
        background: rgba(255, 165, 0, 0.1);
        color: #ffa500;
        border-left: 4px solid #ffa500;
    }
    
    .strength-strong {
        background: rgba(34, 197, 94, 0.1);
        color: #22c55e;
        border-left: 4px solid #22c55e;
    }
    
    /* Requirements Box */
    .requirements-box {
        padding: 1.2rem;
        border-radius: 12px;
        background: rgba(128, 128, 128, 0.05);
        border: 1px solid rgba(128, 128, 128, 0.1);
        margin: 1rem 0;
    }
    
    .requirement-item {
        padding: 0.4rem 0;
        font-size: 0.9rem;
        opacity: 0.8;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Checkbox Styling */
    .stCheckbox {
        margin: 1.5rem 0;
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
    
    /* Login Link */
    .login-link {
        text-align: center;
        margin-top: 2rem;
        padding: 1.2rem;
        border-radius: 12px;
        background: rgba(128, 128, 128, 0.03);
        border: 1px solid rgba(128, 128, 128, 0.1);
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 12px;
        font-weight: 600;
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
<div class="register-header">
    <span class="register-icon">📝</span>
    <h1 class="register-title">Join CartoonifyAI</h1>
    <p class="register-subtitle">Create your free account and start transforming photos</p>
</div>
""", unsafe_allow_html=True)

# Registration Form
with st.container():
    name = st.text_input(
        "Full Name",
        placeholder="John Doe",
        key="register_name",
        help="Your display name on the platform"
    )
    
    email = st.text_input(
        "Email Address",
        placeholder="your.email@example.com",
        key="register_email",
        help="We'll never share your email with anyone"
    )
    
    password = st.text_input(
        "Password",
        type="password",
        placeholder="Create a strong password",
        key="register_password",
        help="Must be at least 8 characters"
    )
    
    # Password strength indicator
    if password:
        strength = 0
        checks = []
        
        if len(password) >= 8:
            strength += 1
            checks.append("✓ 8+ characters")
        else:
            checks.append("✗ 8+ characters")
            
        if any(c.isupper() for c in password):
            strength += 1
            checks.append("✓ Uppercase")
        else:
            checks.append("✗ Uppercase")
            
        if any(c.islower() for c in password):
            strength += 1
            checks.append("✓ Lowercase")
        else:
            checks.append("✗ Lowercase")
            
        if any(c.isdigit() for c in password):
            strength += 1
            checks.append("✓ Number")
        else:
            checks.append("✗ Number")
        
        if strength <= 2:
            st.markdown('<div class="password-strength strength-weak">⚠️ Weak password - Add more requirements</div>', unsafe_allow_html=True)
        elif strength == 3:
            st.markdown('<div class="password-strength strength-medium">⚡ Medium password - Almost there!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="password-strength strength-strong">✅ Strong password - Perfect!</div>', unsafe_allow_html=True)
    
    confirm = st.text_input(
        "Confirm Password",
        type="password",
        placeholder="Re-enter your password",
        key="register_confirm",
        help="Must match the password above"
    )
    
    # Password Requirements
    with st.expander("📋 Password Requirements"):
        st.markdown("""
        <div class="requirements-box">
            <div class="requirement-item">✓ At least 8 characters long</div>
            <div class="requirement-item">✓ Contains uppercase letter (A-Z)</div>
            <div class="requirement-item">✓ Contains lowercase letter (a-z)</div>
            <div class="requirement-item">✓ Contains number (0-9)</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Terms and Conditions
    terms = st.checkbox("I agree to the Terms of Service and Privacy Policy", value=False)
    
    # Register Button
    if st.button("🚀 Create My Account", width="stretch"):
        if not name or not email or not password or not confirm:
            st.error("⚠️ All fields are required")
        
        elif not terms:
            st.warning("⚠️ Please agree to the Terms of Service to continue")
        
        elif not is_valid_email(email):
            st.error("❌ Invalid email format. Please enter a valid email address")
        
        elif not is_strong_password(password):
            st.error("❌ Password must be 8+ characters with uppercase, lowercase, and number")
        
        elif password != confirm:
            st.error("❌ Passwords do not match. Please try again")
        
        else:
            with st.spinner("🔄 Creating your account..."):
                success, msg = register_user(name, email, password)
                if success:
                    st.success(f"✅ {msg}")
                    st.balloons()
                    st.info("👉 Please login with your new credentials")
                    st.markdown("<br>", unsafe_allow_html=True)
                    if st.button("Go to Login", width="stretch"):
                        st.switch_page("pages/Login.py")
                else:
                    st.error(f"❌ {msg}")

# Divider
st.markdown('<div class="divider"><span style="padding: 0 1rem; background: var(--background-color);">OR</span></div>', unsafe_allow_html=True)

# Login Link
st.markdown("""
<div class="login-link">
    <p style="margin: 0; opacity: 0.8; font-size: 1rem;">Already have an account?</p>
    <p style="margin: 0.5rem 0 0 0; opacity: 0.6; font-size: 0.9rem;">Login to continue creating amazing art</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🔐 Login Instead", width="stretch"):
        st.switch_page("pages/Login.py")

# Footer
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; opacity: 0.5; font-size: 0.85rem;">
    <p>© 2026 CartoonifyAI | Transforming memories into art</p>
</div>
""", unsafe_allow_html=True)
