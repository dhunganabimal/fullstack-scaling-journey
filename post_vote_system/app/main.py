from fastapi import FastAPI,APIRouter

from .database import engine
from .routers import posts, users, auth, votes
from .routers.votes import vote
from app import models

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)
@app.get("/")
async def root():
    return {"Voting System Api is Running !!!"}
