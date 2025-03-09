import sqlite3
import os
import sys
from tkinter import messagebox

class Database:
    def __init__(self, database_file="face_recognizer.db"):
        self.database_file = database_file
        self.connection = None
        self.cursor = None

    def connect(self):
        """Establish a connection to the SQLite database"""
        try:
            self.connection = sqlite3.connect(
                self.database_file,
                timeout=20,  # Add timeout of 20 seconds
                isolation_level=None  # Enable autocommit mode
            )
            self.connection.execute('PRAGMA journal_mode=WAL')  # Use Write-Ahead Logging
            self.connection.execute('PRAGMA busy_timeout=10000')  # Set busy timeout to 10 seconds
            self.cursor = self.connection.cursor()
            return True
        except sqlite3.Error as err:
            print(f"Error connecting to SQLite: {err}")
            return False

    def setup_database(self):
        """Set up the database tables"""
        try:
            # Check if the connection is established
            if not self.connection:
                if not self.connect():
                    return False
            
            # Create student table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS student (
                    department TEXT,
                    course TEXT,
                    year TEXT,
                    semester TEXT,
                    student_id TEXT PRIMARY KEY,
                    name TEXT,
                    division TEXT,
                    roll TEXT,
                    gender TEXT,
                    dob TEXT,
                    email TEXT,
                    phone TEXT,
                    address TEXT,
                    teacher_name TEXT,
                    photo_sample TEXT
                )
            ''')
            
            # Create attendance table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS attendance (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id TEXT,
                    roll TEXT,
                    name TEXT,
                    department TEXT,
                    time TEXT,
                    date TEXT,
                    attendance_status TEXT,
                    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE
                )
            ''')
            
            # Create admin table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS admin (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT,
                    user_type TEXT DEFAULT 'user'
                )
            ''')
            
            # Insert default admin user if not exists
            self.cursor.execute('''
                INSERT OR IGNORE INTO admin (username, password, user_type)
                VALUES (?, ?, ?)
            ''', ('admin', 'admin123', 'admin'))
            
            # Create developer table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS developer (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    designation TEXT,
                    email TEXT,
                    phone TEXT,
                    profile_pic TEXT
                )
            ''')
            
            # Create help_support table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS help_support (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    topic TEXT,
                    description TEXT,
                    contact_email TEXT
                )
            ''')
            
            # Insert some initial help topics
            self.cursor.execute('''
                INSERT OR IGNORE INTO help_support (topic, description, contact_email)
                VALUES (?, ?, ?)
            ''', ('Face Recognition Issues', 'If the system is not recognizing your face properly, try updating your photos in better lighting conditions.', 'support@facerec.com'))
            
            self.cursor.execute('''
                INSERT OR IGNORE INTO help_support (topic, description, contact_email)
                VALUES (?, ?, ?)
            ''', ('Attendance Marking', 'If your attendance is not being marked correctly, please contact your administrator.', 'attendance@facerec.com'))
            
            self.cursor.execute('''
                INSERT OR IGNORE INTO help_support (topic, description, contact_email)
                VALUES (?, ?, ?)
            ''', ('Technical Support', 'For any technical issues with the system, please contact the IT department.', 'tech@facerec.com'))
            
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error setting up database: {e}")
            return False

    def execute_query(self, query, params=None):
        """Execute a query with optional parameters"""
        try:
            if not self.connection:
                if not self.connect():
                    return False, "Failed to connect to database"
            
            try:
                if params:
                    self.cursor.execute(query, params)
                else:
                    self.cursor.execute(query)
                
                self.connection.commit()
                return True, "Query executed successfully"
            except sqlite3.OperationalError as e:
                if "database is locked" in str(e):
                    # If database is locked, try to reconnect and retry once
                    self.close()
                    if self.connect():
                        if params:
                            self.cursor.execute(query, params)
                        else:
                            self.cursor.execute(query)
                        self.connection.commit()
                        return True, "Query executed successfully after retry"
                    else:
                        return False, "Database is locked and reconnection failed"
                else:
                    return False, f"Error executing query: {e}"
        except sqlite3.Error as err:
            return False, f"Error executing query: {err}"

    def fetch_data(self, query, params=None):
        """Fetch data from the database"""
        try:
            if not self.connection:
                if not self.connect():
                    return False, "Failed to connect to database", None
            
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            
            result = self.cursor.fetchall()
            return True, "Data fetched successfully", result
        except sqlite3.Error as err:
            return False, f"Error fetching data: {err}", None

    def close(self):
        """Close the database connection"""
        if self.connection:
            self.connection.close()
            self.connection = None
            self.cursor = None

# Function to initialize the database
def initialize_database():
    db = Database()
    if db.connect():
        if db.setup_database():
            messagebox.showinfo("Success", "Database setup completed successfully!")
        else:
            messagebox.showerror("Error", "Failed to set up database tables.")
    else:
        messagebox.showerror("Error", "Failed to connect to SQLite database.")
    db.close()

# If this script is run directly, initialize the database
if __name__ == "__main__":
    initialize_database() 