from account import validaters
from rest_framework.serializers import ValidationError
from rest_framework.status import (
    HTTP_400_BAD_REQUEST
)


class FormatValidator():

  def __init__(self) -> None:
    print('StringValidator')

  @classmethod
  def int_validate(cls,input: int,msg:str):
    validaters.Common.is_none(
        value=input,
        msg=msg
    )
    if not isinstance(input, int):
      raise ValidationError(
          detail={
              "status_code": 0,
              "status_message": msg
          },
          code=HTTP_400_BAD_REQUEST
      )
  @classmethod
  def list_validate(cls,input: list,msg:str):
    validaters.Common.is_none(
        value=input,
        msg=msg
    )
    if not isinstance(input, list):
      raise ValidationError(
          detail={
              "status_code": 0,
              "status_message": msg
          },
          code=HTTP_400_BAD_REQUEST
      ) 

  @classmethod
  def string_validate(cls, input: str, msg: str):
    validaters.Common.is_none(
        value=input,
        msg=msg
    )
    if not isinstance(input, str):
      raise ValidationError(
          detail={
              "status_code": 0,
              "status_message": msg
          },
          code=HTTP_400_BAD_REQUEST
      )
