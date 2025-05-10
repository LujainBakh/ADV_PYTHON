import sqlite3
from pathlib import Path
import hashlib
import os

class DatabaseManager:
    def __init__(self):
        # Create database directory if it doesn't exist
        db_dir = Path("src/database")
        db_dir.mkdir(parents=True, exist_ok=True)
        
        self.db_path = db_dir / "users.db"
        self.init_database()
        self.create_default_user()

    def init_database(self):
        """Initialize the database with required tables"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                college_name TEXT NOT NULL,
                phone_number TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()

    def create_default_user(self):
        """Create the default user if it doesn't exist"""
        try:
            conn = sqlite3.connect(str(self.db_path))
            cursor = conn.cursor()
            
            # Check if default user already exists
            cursor.execute('SELECT id FROM users WHERE email = ?', ('2210002938@iau.edu.sa',))
            if cursor.fetchone() is None:
                # Create default user
                hashed_password = self.hash_password('1234')
                cursor.execute('''
                    INSERT INTO users (email, password, first_name, last_name, college_name, phone_number)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', ('2210002938@iau.edu.sa', hashed_password, 'Lujain', 'Bakhurji', 
                      'College of Computer Science & Technology', '0505800101'))
                conn.commit()
            
            conn.close()
        except Exception as e:
            print(f"Error creating default user: {e}")

    def hash_password(self, password):
        """Hash the password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, email, password, first_name, last_name, college_name, phone_number):
        """Register a new user"""
        try:
            conn = sqlite3.connect(str(self.db_path))
            cursor = conn.cursor()
            
            hashed_password = self.hash_password(password)
            
            cursor.execute('''
                INSERT INTO users (email, password, first_name, last_name, college_name, phone_number)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (email, hashed_password, first_name, last_name, college_name, phone_number))
            
            conn.commit()
            conn.close()
            return True
        except sqlite3.IntegrityError:
            return False  # Email already exists
        except Exception as e:
            print(f"Error registering user: {e}")
            return False

    def verify_user(self, email, password):
        """Verify user credentials"""
        try:
            conn = sqlite3.connect(str(self.db_path))
            cursor = conn.cursor()
            
            hashed_password = self.hash_password(password)
            
            cursor.execute('''
                SELECT id, first_name, last_name FROM users
                WHERE email = ? AND password = ?
            ''', (email, hashed_password))
            
            user = cursor.fetchone()
            conn.close()
            
            return user if user else None
        except Exception as e:
            print(f"Error verifying user: {e}")
            return None

    def get_user_info(self, user_id):
        """Get user information by ID"""
        try:
            conn = sqlite3.connect(str(self.db_path))
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT email, first_name, last_name, college_name, phone_number
                FROM users WHERE id = ?
            ''', (user_id,))
            
            user_info = cursor.fetchone()
            conn.close()
            
            return user_info
        except Exception as e:
            print(f"Error getting user info: {e}")
            return None 

    def update_user_info(self, user_id, email, first_name, last_name, college_name, phone_number):
        """Update user information by ID"""
        try:
            conn = sqlite3.connect(str(self.db_path))
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE users
                SET email = ?, first_name = ?, last_name = ?, college_name = ?, phone_number = ?
                WHERE id = ?
            ''', (email, first_name, last_name, college_name, phone_number, user_id))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error updating user info: {e}")
            return False 