
import numpy as np
import cv2

def encode_face(image_file):
    file_bytes = np.frombuffer(image_file.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)

    img = cv2.resize(img, (100,100))
    encoding = img.flatten()

    return encoding

def compare_faces(enc1, enc2, threshold=3000):
    diff = np.linalg.norm(enc1 - enc2)
    return diff < threshold
