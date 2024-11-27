from config import Settings

class Core:

  def __init__(self, config: Settings):
    self.config= config
    self.service_name = self.config.service_name
    self.modelpath = self.config.modelpath
    self.upload_img_dir = self.config.upload_img_dir
    self.upload_folder = self.config.upload_folder