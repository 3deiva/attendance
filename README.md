
Face Attendance Backend (No Frontend)

Features:
- Register user with face image
- Login with face verification
- Attendance stored in SQLite
- Simple face encoding using OpenCV

Run:
pip install -r requirements.txt
python app.py

Endpoints:
POST /register  (username, image)
POST /login     (username, image)
