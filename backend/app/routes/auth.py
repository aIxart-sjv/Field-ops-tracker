from fastapi import APIRouter, HTTPException
from datetime import datetime

from ..auth.jwt import create_access_token
from ..auth.security import hash_password, verify_password
from ..db.mongo import get_db


router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
def register(user: dict):
    db = get_db()
    if db.users.find_one({"email": user["email"]}):
        raise HTTPException(status_code=400, detail="User exists")

    db.users.insert_one({
        "name": user["name"],
        "email": user["email"],
        "password_hash": hash_password(user["password"]),
        "role": user["role"],
        "created_at": datetime.utcnow()
    })

    return {"message": "user created"}

@router.post("/login")
def login(credentials: dict):
    db = get_db()
    user = db.users.find_one({"email": credentials["email"]})
    if not user or not verify_password(credentials["password"], user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({
        "user_id": str(user["_id"]),
        "role": user["role"]
    })

    return {
        "access_token": token,
        "role": user["role"]
    }
