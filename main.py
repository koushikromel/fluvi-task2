from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from beanie import Document, init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, EmailStr
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = "mongodb://localhost:27017"
DATABASE_NAME = "user_registry"

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]

class User(UserBase):
    id: UUID
    created_at: datetime

class UserModel(Document):
    id: UUID
    name: str
    email: EmailStr
    created_at: datetime

    class Settings:
        collections="users"


async def initialize():
    client = AsyncIOMotorClient(DATABASE_URL)
    await init_beanie(database=client[DATABASE_NAME], document_models=[UserModel])


@app.get("/get_user", response_model=UserBase)
async def get_user(user_id: UUID):
    users = await UserModel.find_one(UserModel.id == user_id)
    return users

@app.put("/update_user/{user_id}", response_model=UserBase)
async def update_user(user_id: UUID, request: UserUpdate):
    user = await UserModel.find_one(UserModel.id == user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if request.name is not None:
        user.name = request.name
    if request.email is not None:
        user.email = request.email
    await user.save()
    return user

@app.delete("/delete_user/{user_id}")
async def delete_user(user_id: UUID):
    user = await UserModel.find_one(UserModel.id == user_id)
    await user.delete()
    return f"User with email: {user.email} is deleted successfully"


@app.post("/create_user", response_model=UserModel)
async def create_user(user: UserCreate):
    user_id = uuid4()
    created_at = datetime.utcnow()
    user_data = UserModel(id=user_id, created_at=created_at, **user.dict())
    await user_data.insert()
    return user_data


@app.on_event("startup")
async def startup_event():
    await initialize()
