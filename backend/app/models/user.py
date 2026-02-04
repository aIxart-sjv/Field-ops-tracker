from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str  # admin | field_officer

class UserInDB(BaseModel):
    id: Optional[str]
    name: str
    email: EmailStr
    password_hash: str
    role: str
    created_at: datetime
