
# Pan Card Processing System using FastAPI and Streamlit

This repository implements an end-to-end solution for processing Pan Card images. The system detects key fields on Pan Card using a coustom YOLOv10 model, extracts text using OCR, and visualizes the results in a Streamlit app. 

### Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Example Output](#example-output)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This project allows users to upload Pan Card images, detect fields such as Pandcard numbers, date of Birth, Name and Father Name using a YOLO model, and extract the detected text using OCR. It provides:
1. A **FastAPI backend** for YOLO inference and OCR processing.
2. A **Streamlit frontend** for uploading images and visualizing the results.

---

## Features

* Detects key Pancard fields using a coustom-trained YOLOv10 model.
* Extracts text from detected bounding boxes using DocTr.
* Displays both the uploaded image and processed JSON response side by side in the Streamlit UI.

---

## Technologies Used

- **YOLOv10** for object detection.
- **DocTr OCR** for text extraction.
- **FastAPI** for the backend API.
- **Streamlit** for the frontend interface.
- **Python**.

---

## Getting Started

### Prerequisites
Ensure you have the following installed:
- Python 3.10 or higher
- pip (Python package manager)
- DocTr (for OCR;)
- A YOLO model trained on Pancard fields (e.g., `best.pt`).

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/RahulJha11/Pand_card_detection_and_OCR.git
   cd Pand_card_detection_and_OCR
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have a YOLO model inside backend/model folder (`best.pt`) ready and place it in the root directory.

---

### Running the Application

#### Step 1: Start the FastAPI Backend
Run the FastAPI server for YOLO inference and OCR processing:
```bash
python backend/app.py
```


The backend API will be accessible at `http://localhost:5000/api/yolo/uploadpancard`.

#### Step 2: Start the Streamlit Frontend
Run the Streamlit app to upload images and view results:
```bash
streamlit run frontend/streamlit_app.py
```
The frontend UI will be available at `http://localhost:8501`.

---


## Usage

1. **Upload Pand Card Image**:
   - Use the Streamlit app to upload an PanCard image (`jpg`, `jpeg`, or `png`).
   
2. **Process Image**:
   - Click the **Process Image** button to send the image to the FastAPI backend.
   - The backend:
     - Runs YOLO inference to detect fields (bounding boxes).
     - Performs OCR on the detected regions to extract text.

3. **View Results**:
   - The **uploaded processed image** will appear on the left side with bonding box.
   - The **JSON response** (containing detected bounding boxes and oCR text) will appear on the right side.

---

## Example Output

#### Input
- Uploaded image:  
![Alt text](frontend/temp_uploads/download.jpg)

#### Output
- **JSON Response**:
  ```json
  [
    {
      "image_path": "D:\\AImonk_assig\\app\\backend\\save_result\\download.jpg",
      "detection": [
        {
          "name": "father",
          "class": 1,
          "confidence": 0.90266,
          "box": {
            "x1": 14.03593,
            "y1": 72.26413,
            "x2": 138.75572,
            "y2": 95.40302
          },
          "ocr_text": "RAJENDRA PRATAP SINGH"
        },
        {
          "name": "name",
          "class": 2,
          "confidence": 0.87311,
          "box": {
            "x1": 13.10176,
            "y1": 49.30516,
            "x2": 134.70937,
            "y2": 68.73293
          },
          "ocr_text": "MAHESH PRATAP -SINGH"
        },
        {
          "name": "dob",
          "class": 0,
          "confidence": 0.73876,
          "box": {
            "x1": 11.69924,
            "y1": 98.85611,
            "x2": 66.73045,
            "y2": 113.40095
          },
          "ocr_text": "06/19 97 -"
        },
        {
          "name": "pan_num",
          "class": 3,
          "confidence": 0.71947,
          "box": {
            "x1": 9.21024,
            "y1": 123.03368,
            "x2": 91.34866,
            "y2": 141.86511
          },
          "ocr_text": "- S WPS0850Q"
        }
      ]
    }
  ]
  ```

- **Detected image**:  
The bounding boxes and extracted text will be displayed on the image using Streamlit.

![Alt text](download.jpg)


---

## Contributing

We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`feature/new-feature`).
3. Commit your changes.
4. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
