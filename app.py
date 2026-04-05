
from flask import Flask, request, jsonify
from models import init_db, add_user, get_user_by_username
from face_utils import encode_face, compare_faces

app = Flask(__name__)
init_db()

@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    image = request.files["image"]
    encoding = encode_face(image)
    add_user(username, encoding)
    return jsonify({"message": "User registered successfully"})

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    image = request.files["image"]

    user = get_user_by_username(username)
    if not user:
        return jsonify({"error": "User not found"}), 404

    encoding = encode_face(image)
    if compare_faces(encoding, user["encoding"]):
        mark_attendance(username)
        return jsonify({"message": "Attendance marked"})
    else:
        return jsonify({"error": "Face not matched"}), 401

if __name__ == "__main__":
    app.run(debug=True)
