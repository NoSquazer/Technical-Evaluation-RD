# FastAPI
from fastapi import APIRouter, Query, Body, Depends, Path, HTTPException
from fastapi.responses import JSONResponse

# SrcUtilities
from src.api_service.schemas import Post_data_response, Get_data_response
from src.database.session import SessionLocal
from src.dependencies import get_db
from src.api_service.service import api_service_service
from src.api_service.utils import valid_target
from src.auth.auth import verify_credentials

api_service_router = APIRouter()


@api_service_router.post("/input/{my_target_field}", response_model=Post_data_response)
def post_data(
    my_target_field: str = Path(..., description="Target field"),
    field_1: str = Body(..., description="Some data..."),
    author: str = Body(..., description="Some author data..."),
    description: str = Body(..., description="Even more data..."),
    my_numeric_field: int = Body(..., description="A numeric field"),
    db: SessionLocal = Depends(get_db),
    user: str = Depends(verify_credentials),
):
    is_valid = valid_target(target=my_target_field)
    if not is_valid:
        raise HTTPException(status_code=400, detail="The target must be valid")

    response = api_service_service.post_data_service(
        db, field_1, author, description, my_numeric_field, my_target_field
    )

    return JSONResponse(content=response)


@api_service_router.get("/get_data/{id}", response_model=Get_data_response)
def get_data(
    id: str = Path(..., description="Id of the data"),
    db: SessionLocal = Depends(get_db),
    user: str = Depends(verify_credentials),
):
    try:
        id = int(id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Id must be a intenger")

    response = api_service_service.get_data_service(db, id)

    if not response:
        raise HTTPException(status_code=404, detail="Data not found")

    return JSONResponse(content=response)
