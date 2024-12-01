from flask import Flask, request, jsonify
import os
import face_recognition
from PIL import Image
import io

app = Flask(__name__)

# Folder to store uploaded images
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Function to save uploaded image and process it
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image part"}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    # Save the uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Process the image to detect faces
    image = face_recognition.load_image_file(file_path)
    face_locations = face_recognition.face_locations(image)

    if not face_locations:
        return jsonify({"error": "No faces found"}), 400

    # Create a folder for each face detected
    for idx, face_location in enumerate(face_locations):
        top, right, bottom, left = face_location
        face_image = image[top:bottom, left:right]
        face_pil_image = Image.fromarray(face_image)
        participant_folder = os.path.join(UPLOAD_FOLDER, f"participant_{idx + 1}")
        if not os.path.exists(participant_folder):
            os.makedirs(participant_folder)
        face_pil_image.save(os.path.join(participant_folder, f"face_{idx + 1}.jpg"))

    return jsonify({"message": "Image processed successfully!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
