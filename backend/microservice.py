from fastapi import FastAPI
from starlette.requests import Request
from fastapi.middleware.cors import CORSMiddleware
import yoloapi
from core import Core


class MicroService:
  def __init__(self, core: Core):
    self.core = core
    self.app = FastAPI(
      title=self.core.config.service_name,
      docs_url=None
    )

    origins = ["*"]
    self.app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    self._configure_routers()

  def get_app(self) -> FastAPI:
      return self.app



  def _configure_routers(self):
    self.app.include_router(
      yoloapi.init(self.core),
      prefix="/api/yolo",
      tags=["document"],

    )