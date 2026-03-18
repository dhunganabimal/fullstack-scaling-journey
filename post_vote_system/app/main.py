from fastapi import FastAPI,APIRouter
from starlette.middleware.cors import CORSMiddleware

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
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"Voting System Api is Running !!!"}
