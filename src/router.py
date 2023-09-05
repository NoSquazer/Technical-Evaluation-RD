# FastAPI
from fastapi import APIRouter

# SrcUtilities
from src.api_service.router import api_service_router


api_router = APIRouter()

api_router.include_router(api_service_router, prefix="/api", tags=["API Service"])
