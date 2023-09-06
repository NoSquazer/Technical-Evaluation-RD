# Pydantic
from pydantic import BaseModel, validator

# FastAPI
from fastapi import HTTPException


class PostDataBody(BaseModel):
    field_1: str
    author: str
    description: str
    my_numeric_field: int

    @validator("field_1", "author", "description", "my_numeric_field", pre=True)
    def validate_fields(cls, value, field):
        # return print(field.type_)
        if not isinstance(value, field.type_):
            raise HTTPException(
                status_code=400,
                detail=f"{field.name} must be a {field.type_.__name__}",
            )
        return value


class PostDataResponse(BaseModel):
    id: int


class GetDataResponse(BaseModel):
    id: int
    field_1: str
    author: str
    description: str
    my_numeric_field: int
