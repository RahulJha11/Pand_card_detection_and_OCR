from fastapi import File, UploadFile
from abc import ABCMeta, abstractmethod
import shutil
from ultralytics import YOLO
from doctr.models import ocr_predictor
from doctr.io import DocumentFile
from config import Settings

import json
import os
import logging
from core import Core

logger = logging.getLogger(__name__)


class Inferenceservice(metaclass=ABCMeta):
  @abstractmethod
  def uploadpancard(self, uploadfile: list[UploadFile] = File(...)):
    pass


class InferenceserviceImpl(Inferenceservice):
  def __init__(self, core: Settings):
    self.core = core
    self.curr_dir = os.getcwd()
    self.upload_img_dir = os.path.join(self.curr_dir , self.core.upload_img_dir )
    self.model = YOLO(os.path.join(self.curr_dir , core.modelpath))
    self.ocr_model = ocr_predictor(det_arch='db_resnet50', reco_arch='crnn_vgg16_bn', pretrained=True)
    self.upload_folder = os.path.join(self.curr_dir, self.core.upload_folder)
    self.to_empty_folfer =  [os.path.join(self.curr_dir,"backend\\crop_image\\dob"), 
                             os.path.join(self.curr_dir,"backend\\crop_image\\father"), 
                             os.path.join(self.curr_dir,"backend\\crop_image\\name"), 
                             os.path.join(self.curr_dir,"backend\\crop_image\\pan_num")]
 

  def save_uploaded_file(self, file, save_dir: str) -> str:
    """Save uploaded file to a directory."""
    try:
      logger.info("into save file function")
      file_path = os.path.join(save_dir, file.filename)
      logger.info(file_path)
      with open(file_path, "wb") as buffer:
          shutil.copyfileobj(file.file, buffer)
      logger.info("save uploadded file into folder")
      return file_path
    except Exception as e:
            return [{
                "message": str(e),
            }]
  

  def yolo_inference(self, image_path: str):
    logger.info("Into yolo inference module")
    file_path = os.path.basename(image_path)
    file_name = [os.path.splitext(file_path)][0][0]
    results = self.model(image_path, show_conf=False)
    logger.info(results)
    img_path = os.path.join(self.curr_dir, f"backend\\save_result\\{file_name}.jpg")
    for res in results:
      res.save(img_path, conf=False, line_width=1, font_size=1)
      res.save_crop(os.path.join(self.curr_dir, "backend\\crop_image\\"))
      res_json = json.loads(res.to_json())
      logger.info(type(res_json))
      logger.info(res_json)

    return res_json, img_path
  
  def img_path(self, folder_path):
    logger.info("Into image_path function")
    name = []
    dob_path = []
    f_path = []
    pan_num_path = []

    for root, dirs, files in os.walk(folder_path):
      if os.path.basename(root) == "name":
        name.extend([os.path.join(root, file) for file in files])
      elif os.path.basename(root) == "dob":
        dob_path.extend([os.path.join(root, file) for file in files])
      elif os.path.basename(root) == "father":
        f_path.extend([os.path.join(root, file) for file in files])
      elif os.path.basename(root) == "pan_num":
        pan_num_path.extend([os.path.join(root, file) for file in files])
    logger.info("finishe image _path")
    logger.info(name[0])

    return [name[0], dob_path[0], f_path[0], pan_num_path[0]]
  
  def del_files(self):
    folders_to_clear = self.to_empty_folfer
    for folder in folders_to_clear:
      for item in os.listdir(folder):
          item_path = os.path.join(folder, item)
          if os.path.isfile(item_path):
              os.remove(item_path)  # Remove the file
          elif os.path.isdir(item_path):
              shutil.rmtree(item_path)  # Remove the subdirectory
    return "All files deleted in crop folder"


  
  def ocr_process(self, img_path):
    logger.info("into ocr proccess")
    model = self.ocr_model
    img_doc = DocumentFile.from_images(img_path)
    ocr_res = model(img_doc)
    logger.info("ocr process finish")
    logger.info(ocr_res.render())
    return ocr_res.render()


  async def uploadpancard(self, uploadfile: list[UploadFile] = File(...)):
    try:
      for file in uploadfile:
        logger.info(file)
        logger.info(self.upload_folder)
        image_path = self.save_uploaded_file(file, self.upload_folder)
        logger.info(image_path)

        detection, file_path = self.yolo_inference(image_path)
        logger.info('detection is finished')
        logger.info(detection)
        img_path = self.img_path(self.upload_img_dir)
        logger.info("got image paths for crop images")
        # detection = json.loads(detection)
        logger.info(type(detection))
        for res in detection:
          logger.info(res)
          if res["name"] == "pan_num":
            res["ocr_text"] = self.ocr_process(img_path[3])
          elif res["name"] == "father":
            res["ocr_text"] = self.ocr_process(img_path[2])
          elif res["name"] == "dob":
            res["ocr_text"] = self.ocr_process(img_path[1])
          elif res["name"] == "name":
            res["ocr_text"] = self.ocr_process(img_path[0])
      result = []
      result.append({"image_path": file_path,
                     "detection":detection})

      self.del_files()
      os.remove(image_path)
      logger.info("API proceess is over Now")
      return result
    except Exception as e:
            return [{
                "message": str(e),
            }]
    