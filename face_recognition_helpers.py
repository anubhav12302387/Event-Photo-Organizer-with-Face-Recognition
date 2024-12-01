import face_recognition
import os

# Directories for reference photos and organized photos
REFERENCE_DIR = './reference_photos'
ORGANISED_DIR = './organised_photos'

def process_uploaded_image(file_path):
    """
    Processes the uploaded image to find a matching face in the reference photos
    and organizes it into the appropriate folder.

    :param file_path: Path to the uploaded image file.
    """
    try:
        uploaded_image = face_recognition.load_image_file(file_path)
        uploaded_face_encodings = face_recognition.face_encodings(uploaded_image)

        if not uploaded_face_encodings:
            print("No faces found in the uploaded image.")
            return {"message": "No faces found in the uploaded image."}

        uploaded_face_encoding = uploaded_face_encodings[0]

        for reference_image_name in os.listdir(REFERENCE_DIR):
            reference_image_path = os.path.join(REFERENCE_DIR, reference_image_name)


            if not reference_image_name.lower().endswith(('png', 'jpg', 'jpeg')):
                continue

            reference_image = face_recognition.load_image_file(reference_image_path)
            reference_face_encodings = face_recognition.face_encodings(reference_image)

            if not reference_face_encodings:
                print(f"No faces found in reference image: {reference_image_name}")
                continue

            reference_face_encoding = reference_face_encodings[0]

            
            results = face_recognition.compare_faces([reference_face_encoding], uploaded_face_encoding)

            if results[0]:
               
                matched_dir = os.path.join(ORGANISED_DIR, reference_image_name.split('.')[0])
                os.makedirs(matched_dir, exist_ok=True)

                
                new_file_path = os.path.join(matched_dir, os.path.basename(file_path))
                os.rename(file_path, new_file_path)
                print(f"Moved {file_path} to {new_file_path}")
                return {"message": f"File moved to {matched_dir}", "matched_with": reference_image_name}

        print("No matching faces found.")
        return {"message": "No matching faces found."}

    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": str(e)}
