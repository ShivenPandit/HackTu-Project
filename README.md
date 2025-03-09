# Face Recognition Attendance System

A comprehensive face recognition-based attendance management system built with Python. This system automates the process of taking attendance using facial recognition technology.

## Features

- 👤 Face Detection and Recognition
- 📝 Automated Attendance Recording
- 🔐 Secure Login System
- 👥 Student Registration
- 📊 Attendance Management
- 📋 CSV Export Functionality
- 💾 SQLite Database Integration
- 👨‍💼 Admin Dashboard

## Tech Stack

- Python
- OpenCV (Face Detection and Recognition)
- SQLite (Database)
- Tkinter (GUI)
- Haar Cascade Classifier

## Project Structure

```
├── Main.py                 # Main application entry point
├── login.py               # Login system implementation
├── register.py            # User registration module
├── attendance.py          # Attendance management system
├── face_recognition.py    # Face recognition implementation
├── database_sqlite.py     # Database operations
├── Student.py             # Student management module
├── train.py              # Model training module
├── Data/                 # Training data directory
├── myImages/             # Image storage
└── attendance.csv        # Attendance records
```

## Setup Instructions

1. Clone the repository
```bash
git clone <repository-url>
```

2. Install required dependencies
```bash
pip install opencv-python
pip install numpy
pip install pandas
pip install pillow
```

3. Run the application
```bash
python Main.py
```

## Usage

1. **Admin Login**: Use the login system to access the admin dashboard
2. **Register Students**: Add new students with their details and face data
3. **Train Model**: Train the face recognition model with registered faces
4. **Take Attendance**: Use the face recognition system to mark attendance
5. **View Reports**: Access attendance reports and export data as needed

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
