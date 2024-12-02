from flask import Flask, request, jsonify, render_template
import os
from werkzeug.utils import secure_filename
import face_recognition

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = './uploads'
REFERENCE_DIR = './reference_photos'
ORGANISED_DIR = './organised_photos'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure required directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REFERENCE_DIR, exist_ok=True)
os.makedirs(ORGANISED_DIR, exist_ok=True)

# Helper function to validate file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to process uploaded images
def process_uploaded_image(file_path):
    try:
        uploaded_image = face_recognition.load_image_file(file_path)
        uploaded_face_encodings = face_recognition.face_encodings(uploaded_image)

        if not uploaded_face_encodings:
            return {"message": "No faces found in the uploaded image."}

        uploaded_face_encoding = uploaded_face_encodings[0]

        for reference_image_name in os.listdir(REFERENCE_DIR):
            reference_image_path = os.path.join(REFERENCE_DIR, reference_image_name)

            if not reference_image_name.lower().endswith(('png', 'jpg', 'jpeg')):
                continue

            reference_image = face_recognition.load_image_file(reference_image_path)
            reference_face_encodings = face_recognition.face_encodings(reference_image)

            if not reference_face_encodings:
                continue

            reference_face_encoding = reference_face_encodings[0]

            results = face_recognition.compare_faces([reference_face_encoding], uploaded_face_encoding)

            if results[0]:
                matched_dir = os.path.join(ORGANISED_DIR, reference_image_name.split('.')[0])
                os.makedirs(matched_dir, exist_ok=True)

                new_file_path = os.path.join(matched_dir, os.path.basename(file_path))
                os.rename(file_path, new_file_path)
                return {
                    "message": f"File moved to {matched_dir}",
                    "matched_with": reference_image_name,
                    "preview_url": f"/preview/{reference_image_name}"
                }

        return {"message": "No matching faces found."}

    except Exception as e:
        return {"error": str(e)}

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')  # Renders the index.html template

# Route to handle file uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Invalid file type"}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    # Process the uploaded image
    result = process_uploaded_image(file_path)
    return jsonify(result)

# Route to preview reference images
@app.route('/preview/<filename>', methods=['GET'])
def preview_file(filename):
    reference_image_path = os.path.join(REFERENCE_DIR, filename)
    if os.path.exists(reference_image_path):
        return app.send_static_file(reference_image_path)
    return jsonify({"error": "Image not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
