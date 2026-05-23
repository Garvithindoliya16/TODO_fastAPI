from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.connection import engine, Base
from routers.todo_router import router as todo_router
from routers.auth_router import router as auth_router
from models import user_model
from models import todo_model

app = FastAPI()


app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "https://fastapitodo.netlify.app"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


app.include_router(todo_router)
app.include_router(auth_router)