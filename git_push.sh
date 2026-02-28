#!/bin/bash

# CartoonifyAI - Git Setup Script
# GitHub Username: ArpitSingh8

echo "🚀 Starting Git setup for CartoonifyAI..."
echo ""

# Step 1: Initialize Git repository
echo "📦 Initializing Git repository..."
git init

# Step 2: Add all files
echo "📁 Adding all files..."
git add .

# Step 3: Create initial commit
echo "💾 Creating initial commit..."
git commit -m "Initial commit: Complete CartoonifyAI project

- Implemented user authentication system with bcrypt
- Created SQLite database with users table
- Built registration and login pages with validation
- Developed user dashboard with session management
- Added route protection for authenticated pages
- Implemented image transformation with OpenCV
- Designed modern glassmorphism UI
- Added comprehensive documentation"

# Step 4: Add remote origin
echo "🔗 Adding remote origin..."
git remote add origin https://github.com/ArpitSingh8/CartoonifyAI.git

# Step 5: Rename branch to main
echo "🌿 Setting branch to main..."
git branch -M main

# Step 6: Push to GitHub
echo "⬆️ Pushing to GitHub..."
git push -u origin main

echo ""
echo "✅ Done! Your project is now on GitHub!"
echo "🌐 View it at: https://github.com/ArpitSingh8/CartoonifyAI"
