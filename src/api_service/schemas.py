# Pydantic
from pydantic import BaseModel


class Post_data_response(BaseModel):
    id: int


class Get_data_response(BaseModel):
    id: int
    field_1: str
    author: str
    description: str
    my_numeric_field: int


class DataModel(BaseModel):
    field_1: str
    author: str
    description: str
    my_numeric_field: int
