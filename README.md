# 🎨 AI Image Cartoon Transformer - CartoonifyAI

A modern web application that transforms your photos into stunning cartoon artwork using AI-powered image processing with complete user authentication and dashboard management.

## ✨ Features

### User Management & Authentication
- 🔐 **Secure Registration & Login** - Complete authentication system with password hashing
- 📊 **User Dashboard** - Personalized dashboard as the main hub after login
- 🛡️ **Route Protection** - Protected pages accessible only to authenticated users
- 🚪 **Session Management** - Secure logout with session clearing
- 👤 **Account Details** - View and manage profile information

### Core Functionality
- 🎨 **AI-Powered Cartoon Transformation** - Convert photos to cartoons instantly
- ⚙️ **Customizable Settings** - Adjust edge strength and color smoothing
- 📥 **High-Quality Downloads** - Save your artwork in PNG format
- 🖼️ **Real-time Preview** - See original and cartoon side-by-side

### Design
- 🎯 **Modern UI/UX** - Clean, gradient-based glassmorphism design
- 📱 **Responsive Layout** - Wide layout with organized components
- 🎭 **Theme Adaptive** - Perfect in both light and dark modes
- ✨ **Smooth Animations** - Hover effects and transitions

## 🚀 Installation

```bash
pip install -r requirements.txt
```

## ▶️ Run

```bash
streamlit run home.py
```

## 📁 Project Structure

```
├── home.py                    # Landing page (redirects authenticated users)
├── backend/
│   ├── auth.py               # Authentication logic
│   ├── database.py           # Database operations
│   └── __init__.py
├── pages/
│   ├── Login.py              # Login page
│   ├── Register.py           # Registration page
│   ├── Dashboard.py          # User dashboard (protected)
│   └── Transform.py          # Image transformation page (protected)
├── utils/
│   ├── validators.py         # Input validation
│   └── __init__.py
├── assets/
│   └── logo.png              # Application logo
└── requirements.txt          # Dependencies
```

## 🎯 User Flow

1. **Landing Page** (home.py) - Welcome page with features showcase
2. **Register/Login** - Create account or login via sidebar
3. **Dashboard** - Main hub after login with:
   - Welcome message with user's name
   - Quick action buttons (Transform Image, Settings)
   - Account details display
   - User statistics
   - Logout functionality
4. **Transform Page** - Upload and transform images with:
   - File uploader
   - Advanced controls (edge strength, color smoothing)
   - Side-by-side comparison
   - Download functionality
5. **Route Protection** - Non-authenticated users redirected to login

## 🔒 Security Features

- Password hashing with bcrypt
- Session state management
- Route protection on all protected pages
- Secure logout with session clearing
- Input validation for email and password

## 🛠️ Technologies

- **Streamlit** - Web framework
- **OpenCV** - Image processing
- **Pillow** - Image handling
- **bcrypt** - Password hashing
- **SQLite** - Database

## 📝 License

Open source project for educational purposes.