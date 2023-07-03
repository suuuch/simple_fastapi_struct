from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from databases import schemas, cruds
from dependencies import get_db

router = APIRouter()


@router.post("/users/", tags=["users"], response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = cruds.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return cruds.create_user(db=db, user=user)


@router.get("/users/", tags=["users"], response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = cruds.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", tags=["users"], response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = cruds.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/users/me", tags=["users"], response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = cruds.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
