from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import genres, artists, albums
from app.database import engine
from app import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Music Catalog API")

origins = [
        "http://frontend:3000",
        "http://51.250.17.187:3000/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(genres.router, prefix="/genres", tags=["Genres"])
app.include_router(artists.router, prefix="/artists", tags=["Artists"])
app.include_router(albums.router, prefix="/albums", tags=["Albums"])

@app.get("/health")
def health_check():
    return {"status": "ok"}

