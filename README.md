# PixTrove with Face Recognition  

This project automates the process of organizing event photos by recognizing participants' faces. During registration, participants provide a reference photo. After the event, the system processes the uploaded photos, matches faces with the reference images, and organizes them into separate folders named after each participant.  

## Key Features  
- **Face Recognition**: Identifies faces in event photos using a reference image.  
- **Automated Organization**: Creates folders named after participants and sorts their photos into respective folders.  
- **Manual Review**: Flags unmatched faces for manual categorization.  
- **Efficient Workflow**: Saves time by eliminating the need for manual photo sorting.  

## How It Works  
1. **Registration**:  
   - Participants upload a recent photo during event registration.  
   - The system stores these reference images labeled with participants' names or IDs.  

2. **Photo Upload**:  
   - After the event, the cameraman uploads the folder of event photos to the system.  

3. **Photo Processing**:  
   - The system scans each photo and matches detected faces with the reference images.  
   - Matches are sorted into individual folders named after the participants.  

4. **Output**:  
   - Organized photo folders are ready for download or distribution.  

## Tech Stack  
- **Programming Language**: Python  
- **Libraries**:  
  - [OpenCV](https://opencv.org/) or [Dlib](http://dlib.net/) for face detection and recognition.  
  - [DeepFace](https://github.com/serengil/deepface) for enhanced face matching capabilities.  
- **Framework**: Flask/Django (optional, for a web interface).  
- **Storage**: Local file system or cloud storage for scalable deployment.

- **Frontend**:
  - **NextJS**
  - **Tailwind CSS**

## Installation  

1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/anubhav12302387/Event-Photo-Organizer-with-Face-Recognition.git
   cd event-photo-organizer  

2. **Set Up a Virtual Environment:**
   ```bash
     python3 -m venv venv 

3. **Install Dependencies:**
   ```bash
       pip install -r requirements.txt  

4. **Run the Script:**
   ```bash
   python main.py 

## Usage

1. Add participant reference photos to the reference_images directory.
2. Upload event photos to the event_photos directory.
3. Run the script to process and organize photos.
4. The output will be saved in the output_photos directory, with separate folders for each participant.

## Contributing
Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## Organize your event memories effortlessly! 🎉
  ```bash
  
Let me know if you want further adjustments!


