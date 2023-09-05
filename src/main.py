# Python
from functools import lru_cache

# FastAPI
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

# SrcUtilities
from src.router import api_router
from src.config import Settings

settings = Settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Techinal evaluation for RD",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@lru_cache()
def get_settings():
    return Settings()


@app.on_event("shutdown")
def close_db_connection():
    from src.dependencies import get_db

    db = get_db()
    db.close()


app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/", response_class=RedirectResponse, include_in_schema=False)
async def docs():
    return RedirectResponse(url="/docs")
