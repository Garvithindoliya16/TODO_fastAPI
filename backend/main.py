from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from routers.todo_router import router as todo_router
from routers.auth_router import router as auth_router


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