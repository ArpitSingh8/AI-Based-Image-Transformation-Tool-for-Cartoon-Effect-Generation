# 🎨 AI Image Cartoon Transformer - CartoonifyAI

A modern web application that transforms your photos into stunning cartoon artwork using AI-powered image processing with complete user authentication and dashboard management.

## ✨ Features

### User Management & Authentication
- 🔐 **Secure Registration & Login** - Complete authentication system with password hashing
- 📊 **User Dashboard** - Personalized dashboard as the main hub after login
- 🛡️ **Route Protection** - Protected pages accessible only to authenticated users
- 🚪 **Session Management** - Secure logout with session clearing
- 👤 **Account Details** - View and manage profile information

### Advanced Image Processing (Week 3-4)
- 🎨 **Multiple Cartoon Styles** - 5 different artistic styles to choose from:
  - **Classic Cartoon** - Bold edges with smooth colors
  - **Pencil Sketch** - Black and white detailed sketch
  - **Colored Pencil** - Sketch with original colors
  - **Watercolor** - Soft, painted look
  - **Oil Painting** - Thick brush strokes effect
- ⚙️ **Customizable Parameters** - Fine-tune each style with advanced controls
- 🔄 **Side-by-Side Comparison** - View original and transformed images together
- 📥 **Instant Download** - Download transformed images before any payment
- 🚀 **Optimized Processing** - Works efficiently on all image types and sizes
- 🎯 **High-Quality Output** - Professional-grade transformations

### Technical Implementation
- 🔍 **Edge Detection** - Adaptive thresholding for precise outlines
- 🎨 **Bilateral Filtering** - Edge-preserving color smoothing
- 🌈 **Color Quantization** - K-means clustering for cartoon colors
- 📐 **Image Preprocessing** - Automatic optimization for different sizes
- 💾 **Memory Management** - Efficient handling of large images

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
- **OpenCV** - Advanced image processing with multiple algorithms
- **Pillow** - Image handling and manipulation
- **bcrypt** - Secure password hashing
- **SQLite** - Lightweight database
- **NumPy** - Numerical operations for image processing

## 📝 License

Open source project for educational purposes.