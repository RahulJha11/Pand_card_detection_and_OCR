# Invoice Processing System using FastAPI and Streamlit

This repository implements an end-to-end solution for processing invoice images. The system detects key fields on invoices using a YOLO model, extracts text using OCR, and visualizes the results in a Streamlit app.


## Table of Contents
* Overview
* Features
* Technologies Used
* Getting Started
* Prerequisites
* Installation
* Running the Application
* Project Structure
* Usage
* Example Output
* Future Enhancements
* Contributing
* License


## Overview
This project allows users to upload pancard  images, detect fields such as name, date of birth, Father Name and Pancard Number using a YOLOv10 model, and extract the detected text using OCR. It provides:

1. A FastAPI backend for YOLO inference and OCR processing.
2. A Streamlit frontend for uploading images and visualizing the results.

## Features
* Detects key Pancard fields using a coustom-trained YOLOv10 model.
* Extracts text from detected bounding boxes using DocTr.
* Displays both the uploaded image and processed JSON response side by side in the Streamlit UI.


## Technologies Used
* YOLOv10 for object detection.
* DocTr OCR for text extraction.
* FastAPI for the backend API.
* Streamlit for the frontend interface.



# Getting Started
## Prerequisites
Ensure you have the following installed:

* Python 3.10 or higher
* pip (Python package manager)
* DocTr (for OCR)
* A YOLO model trained on Pan card fields (e.g., best.pt).


## Installation
1. Clone the repository:
