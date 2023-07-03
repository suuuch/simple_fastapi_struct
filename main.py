from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from dependencies import get_query_token, oauth2_scheme
from internal import admin
from routers import items, users

app = FastAPI()

app.include_router(users.router)

app.include_router(items.router,
                   prefix="/items",
                   tags=["items"],
                   responses={404: {"description": "Not found"}},
                   dependencies=[Depends(get_query_token)])

app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(oauth2_scheme)],
    responses={418: {"description": "I'm a teapot"}},
)

app.mount("/static", StaticFiles(directory="static"), name="static")
