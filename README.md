# Face Recognition Attendance System

An automated **attendance system** that leverages **Face Recognition** using Python, OpenCV, and Deep Learning. This system captures real-time video, recognizes faces, and logs attendance efficiently in a **MySQL** database.

## 📌 Features

- 🎥 Real-time face detection and recognition using OpenCV
- 🤖 Deep Learning models for accurate face matching
- 💾 MySQL integration for secure and persistent attendance logging
- 📊 Auto-generated attendance reports
- 🧠 Optimized using NumPy for high-performance computation

---

## 🚀 Tech Stack

| Technology | Description |
|------------|-------------|
| 🐍 Python   | Core language |
| 📷 OpenCV   | Real-time face detection and image processing |
| 🤖 Deep Learning | Face recognition using pre-trained models (e.g., FaceNet, Dlib, etc.) |
| 🗃 MySQL    | Database to store attendance logs |
| 🔣 NumPy    | Efficient numerical computations |

---

## 📁 Project Structure

```bash
face-recognition-attendance/
├── dataset/              # Stores training images
├── recognizer/           # Face encoding and model
├── attendance/           # Logs and reports
├── main.py               # Main application script
├── db_config.py          # MySQL credentials and config
├── requirements.txt      # Python dependencies
└── README.md
