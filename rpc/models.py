from pydantic import BaseModel
import json

class StringHandle(BaseModel):
    input: str


class Request(BaseModel):
    input: str
    timestamp: int


class Answer(BaseModel):
    output: str
    timestamp: int

def cls_to_json(cls: BaseModel) -> str:
    return json.dumps(cls.model_dump(), indent=2)

def json_to_cls(cls: BaseModel, data: str) -> BaseModel:
    data = json.loads(data)
    return cls(**data)