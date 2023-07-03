from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.post("/")
async def update_admin():
    return {"message": "Admin getting schwifty"}
