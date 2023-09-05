# FastAPI
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

# SrcUtilities
from src.router import api_router


app = FastAPI(
    title="RD Test",
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


@app.on_event("shutdown")
def close_db_connection():
    from src.dependencies import get_db

    db = get_db()
    db.close()


app.include_router(api_router, prefix="/api")


@app.get("/", response_class=RedirectResponse, include_in_schema=False)
async def docs():
    return RedirectResponse(url="/docs")
