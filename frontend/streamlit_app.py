import streamlit as st
import requests
import os
from PIL import Image
import json





FASTAPI_URL = "http://127.0.0.1:5000/api/yolo/uploadpancard"

root_dir = os.getcwd()
UPLOAD_DIR = os.path.join(root_dir, "frontend\\temp_uploads")

os.makedirs(UPLOAD_DIR, exist_ok=True)


def upload_and_processing_img(image_file):
  try:
   
    # """Upload image to FastAPI endpoint and get the JSON response."""
    file_path = os.path.join(UPLOAD_DIR, image_file.name)
    with open(file_path, "wb") as f:
      f.write(image_file.getbuffer())

    with open(file_path, "rb") as f:
      files = [("uploadfile", (image_file.name, open(file_path, "rb"), "image/jpeg"))]


    headers = {}
    payload = {}

    res = requests.post(url= FASTAPI_URL, headers=headers, data=payload, files= files)
    res = res.text
    print(type(res))
    print(json.loads(res))
    print(res)
    return json.loads(res)
    
  except Exception as e:
        st.error(f"An error occurred: {e}")
        return None
  

#  Streamlit UI
st.title("Pand card Data Extractor")
st.write("Upload an pan card image to detect fields and extract text.")

# File uploader

uploaded_image = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_image:


  # process the image
  if st.button("Process Image"):
    with st.spinner("Processing..."):
      result = upload_and_processing_img(uploaded_image)
      print("FastApi process is done")
      print(result)
      

    if result:
      # Display JSON response
      print("Display JSON response")
      col1, col2 = st.columns(2)
      json_res = json.loads(result['data'])
      print("json result")
      print(json_res)

      with col1:
        st.subheader("Image with Detections")
        st.image(Image.open(json_res[0]["image_path"]), caption="Image with Detections", use_container_width=True)

      with col2:
        st.subheader("JSON Response")
        st.json(json_res)


  

      