from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app import user, database

app = FastAPI(title="User Registry")

app.include_router(user.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    await database.initialize()
