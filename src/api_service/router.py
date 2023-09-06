# FastAPI
from fastapi import APIRouter, Body, Depends, Path, HTTPException
from fastapi.responses import JSONResponse

# SrcUtilities
from src.api_service.schemas import PostDataResponse, GetDataResponse, PostDataBody
from src.database.session import SessionLocal
from src.dependencies import get_db
from src.api_service.service import api_service_service
from src.api_service.utils import validate_target
from src.auth.auth import verify_credentials

api_service_router = APIRouter()


@api_service_router.post("/input/{my_target_field}", response_model=PostDataResponse)
def post_data(
    my_target_field: str = Path(..., description="Target field"),
    data: PostDataBody = Body(..., description="Required fields"),
    db: SessionLocal = Depends(get_db),
    user: str = Depends(verify_credentials),
):
    is_target_valid = validate_target(target=my_target_field)
    if not is_target_valid:
        raise HTTPException(
            status_code=400, detail=f"{my_target_field} is not a valid field"
        )

    response = api_service_service.post_data_service(
        db,
        data.field_1,
        data.author,
        data.description,
        data.my_numeric_field,
        my_target_field,
    )

    return JSONResponse(content=response)


@api_service_router.get("/get_data/{id}", response_model=GetDataResponse)
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
