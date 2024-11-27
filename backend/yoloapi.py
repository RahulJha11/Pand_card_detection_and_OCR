from fastapi import APIRouter, status, Response, Request, File, UploadFile
from fastapi.exceptions import HTTPException
import logger
from inference import Inferenceservice, InferenceserviceImpl
import json
from core import Core
from enum import Enum
from pydantic import BaseModel


class ResponseStatus(str, Enum):
    success = "success"
    error = "error"


class Response(BaseModel):
    status: str
    code: int
    message: str=''
    data: str



def init(core:Core) -> APIRouter:
  router = APIRouter()
  inferenceService : Inferenceservice = InferenceserviceImpl(core)

  @router.post(
    "/uploadpancard",
    response_model=Response,
    status_code=status.HTTP_201_CREATED,
  )

  async def uploadpancard(request: Request, uploadfile: list[UploadFile] = File(...)) -> Response:
    try:
      result = await inferenceService.uploadpancard(uploadfile)

    except Exception as e:
      logger.exception(e)
      raise HTTPException(status_code=500, detail="Internal Server Error")

    return Response(
      status=ResponseStatus.success,
      code=200,
      data = json.dumps(result,  indent=4)
    )
  
  return router