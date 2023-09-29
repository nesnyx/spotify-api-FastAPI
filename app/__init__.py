from fastapi import FastAPI
from app.utils import router
app = FastAPI(title="Spotify")

app.include_router(router)