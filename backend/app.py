import uvicorn
import faulthandler
from microservice import MicroService
from config import Settings
from core import Core
faulthandler.enable()

config = Settings()
core = Core(config)
microservice_app = MicroService(core).get_app()

uvicorn.run(microservice_app, port=5000)