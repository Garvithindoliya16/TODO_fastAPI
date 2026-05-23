from pydantic import BaseModel


class TodoCreate(BaseModel):
    task: str
    description:str


class TodoResponse(BaseModel):
    id: int
    task: str
    completed: bool

    class Config:
        from_attributes = True