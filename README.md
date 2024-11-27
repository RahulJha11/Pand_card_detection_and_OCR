# Writing the README.md file to the project directory

readme_content = """
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

- Detects key invoice fields using a pre-trained YOLO model.
- Extracts text from detected bounding boxes using Tesseract or EasyOCR.
- Displays both the uploaded image and processed JSON response side by side in the Streamlit UI.
- Supports dynamic switching between Tesseract and EasyOCR for OCR tasks.

---

## Technologies Used

- **YOLOv8** for object detection.
- **Tesseract OCR** and **EasyOCR** for text extraction.
- **FastAPI** for the backend API.
- **Streamlit** for the frontend interface.
- **Python** (with libraries such as `httpx`, `opencv-python`, and `matplotlib`).

---

## Getting Started

### Prerequisites
Ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)
- Tesseract (for OCR; install [here](https://github.com/tesseract-ocr/tesseract))
- A YOLO model trained on invoice fields (e.g., `best.pt`).

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/invoice-processing.git
   cd invoice-processing
