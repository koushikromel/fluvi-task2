from beanie import init_beanie
from .models import UserModel
from motor.motor_asyncio import AsyncIOMotorClient


DATABASE_URL = "mongodb://localhost:27017"
DATABASE_NAME = "user_registry"

async def initialize():
    client = AsyncIOMotorClient(DATABASE_URL)
    await init_beanie(database=client[DATABASE_NAME], document_models=[UserModel])
