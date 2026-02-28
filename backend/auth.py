import bcrypt
import sqlite3
from datetime import datetime
from backend.database import get_connection

# Hash Password
def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

# Verify Password
def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

# Register User
def register_user(name, email, password):
    conn = get_connection()
    cursor = conn.cursor()

    hashed_password = hash_password(password)

    try:
        cursor.execute("""
        INSERT INTO users (name, email, password, created_at)
        VALUES (?, ?, ?, ?)
        """, (name, email, hashed_password, datetime.now()))

        conn.commit()
        return True, "Registration successful!"

    except sqlite3.IntegrityError:
        return False, "Email already exists."

    finally:
        conn.close()

# Login User
def login_user(email, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()

    conn.close()

    if user and verify_password(password, user[3]):
        return True, user

    return False, "Invalid email or password."