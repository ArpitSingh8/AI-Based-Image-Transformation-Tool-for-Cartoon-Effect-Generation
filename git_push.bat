@echo off
REM CartoonifyAI - Git Setup Script for Windows
REM GitHub Username: ArpitSingh8

echo.
echo ========================================
echo   CartoonifyAI - Git Setup
echo ========================================
echo.

echo [1/6] Initializing Git repository...
git init
if %errorlevel% neq 0 (
    echo ERROR: Git initialization failed
    pause
    exit /b 1
)

echo.
echo [2/6] Adding all files...
git add .
if %errorlevel% neq 0 (
    echo ERROR: Failed to add files
    pause
    exit /b 1
)

echo.
echo [3/6] Creating initial commit...
git commit -m "Initial commit: Complete CartoonifyAI project - Implemented user authentication system with bcrypt - Created SQLite database with users table - Built registration and login pages with validation - Developed user dashboard with session management - Added route protection for authenticated pages - Implemented image transformation with OpenCV - Designed modern glassmorphism UI - Added comprehensive documentation"
if %errorlevel% neq 0 (
    echo ERROR: Failed to create commit
    pause
    exit /b 1
)

echo.
echo [4/6] Adding remote origin...
git remote add origin https://github.com/ArpitSingh8/CartoonifyAI.git
if %errorlevel% neq 0 (
    echo WARNING: Remote might already exist, continuing...
    git remote set-url origin https://github.com/ArpitSingh8/CartoonifyAI.git
)

echo.
echo [5/6] Setting branch to main...
git branch -M main
if %errorlevel% neq 0 (
    echo ERROR: Failed to rename branch
    pause
    exit /b 1
)

echo.
echo [6/6] Pushing to GitHub...
git push -u origin main
if %errorlevel% neq 0 (
    echo ERROR: Failed to push to GitHub
    echo.
    echo Make sure you have:
    echo 1. Created the repository on GitHub: https://github.com/new
    echo 2. Set up your Git credentials
    echo 3. Have internet connection
    pause
    exit /b 1
)

echo.
echo ========================================
echo   SUCCESS! Project pushed to GitHub
echo ========================================
echo.
echo View your project at:
echo https://github.com/ArpitSingh8/CartoonifyAI
echo.
pause
