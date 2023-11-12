from fastapi import APIRouter, HTTPException
from .schemas import UserBase, UserCreate, UserUpdate
from .models import UserModel
from uuid import UUID, uuid4
from datetime import datetime


router = APIRouter(tags=["User"], prefix="/user")

@router.post("/create", response_model=UserModel)
async def create_user(user: UserCreate):
    user_id = uuid4()
    created_at = datetime.utcnow()
    user_data = UserModel(id=user_id, created_at=created_at, **user.dict())
    await user_data.insert()
    return user_data

@router.get("/get", response_model=UserBase)
async def get_user(user_id: UUID):
    users = await UserModel.find_one(UserModel.id == user_id)
    return users

@router.put("/update/{user_id}", response_model=UserBase)
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

@router.delete("/delete/{user_id}")
async def delete_user(user_id: UUID):
    user = await UserModel.find_one(UserModel.id == user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    await user.delete()
    return {"message": f"User with email: {user.email} is deleted successfully"}