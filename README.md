
# Invoice Processing System using FastAPI and Streamlit

This repository implements an end-to-end solution for processing invoice images. The system detects key fields on invoices using a YOLO model, extracts text using OCR, and visualizes the results in a Streamlit app. 

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
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This project allows users to upload invoice images, detect fields such as invoice numbers, dates, and amounts using a YOLO model, and extract the detected text using OCR. It provides:
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
   git clone https://github.com/yourusername/invoice-processing.git
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

1. **Upload Invoice Image**:
   - Use the Streamlit app to upload an invoice image (`jpg`, `jpeg`, or `png`).
   
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
![Uploaded Image Example](https://via.placeholder.com/400x200)

#### Output
- **JSON Response**:
  ```json
  [
      {
          "image": "invoice1.jpg",
          "detections": [
              {
                  "class_id": 0,
                  "confidence": 0.95,
                  "bounding_box": {
                      "x_min": 100,
                      "y_min": 50,
                      "x_max": 200,
                      "y_max": 80
                  },
                  "text": "INV12345"
              },
              {
                  "class_id": 1,
                  "confidence": 0.92,
                  "bounding_box": {
                      "x_min": 150,
                      "y_min": 100,
                      "x_max": 250,
                      "y_max": 130
                  },
                  "text": "2024-11-23"
              }
          ]
      }
  ]

  ```

- **Visualized Image**:
  The bounding boxes and extracted text will be displayed on the image using Streamlit.


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
