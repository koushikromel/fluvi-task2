from beanie import Document
from uuid import UUID
from pydantic import EmailStr
from datetime import datetime


class UserModel(Document):
    id: UUID
    name: str
    email: EmailStr
    created_at: datetime

    class Settings:
        collections="users"