from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.AlbumOut)
def create_album(album: schemas.AlbumCreate, db: Session = Depends(get_db)):
    return crud.create_album(db, album)

@router.get("/", response_model=list[schemas.AlbumOut])
def read_albums(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_albums(db, skip, limit)

@router.get("/{album_id}", response_model=schemas.AlbumOut)
def read_album(album_id: int, db: Session = Depends(get_db)):
    db_album = crud.get_album(db, album_id)
    if not db_album:
        raise HTTPException(status_code=404, detail="Album not found")
    return db_album

@router.put("/{album_id}", response_model=schemas.AlbumOut)
def update_album(album_id: int, album: schemas.AlbumCreate, db: Session = Depends(get_db)):
    db_album = crud.update_album(db, album_id, album)
    if not db_album:
        raise HTTPException(status_code=404, detail="Album not found")
    return db_album

@router.delete("/{album_id}")
def delete_album(album_id: int, db: Session = Depends(get_db)):
    crud.delete_album(db, album_id)
    return {"detail": "Album deleted"}

