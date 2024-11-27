import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  service_name: str
  modelpath:str
  upload_img_dir: str
  upload_folder: str


  # model_config = SettingsConfigDict(env_file=".env", extra='ignore')
  class Config:
        env_file = ".env"