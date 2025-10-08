from sqlalchemy.orm import Session
from app import models, schemas

# Genres
def create_genre(db: Session, genre: schemas.GenreCreate):
    db_genre = models.Genre(name=genre.name)
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre

def get_genres(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Genre).offset(skip).limit(limit).all()

def get_genre(db: Session, genre_id: int):
    return db.query(models.Genre).filter(models.Genre.id == genre_id).first()

def update_genre(db: Session, genre_id: int, genre: schemas.GenreCreate):
    db_genre = db.query(models.Genre).filter(models.Genre.id == genre_id).first()
    if db_genre:
        db_genre.name = genre.name
        db.commit()
        db.refresh(db_genre)
    return db_genre

def delete_genre(db: Session, genre_id: int):
    db_genre = db.query(models.Genre).filter(models.Genre.id == genre_id).first()
    if db_genre:
        db.delete(db_genre)
        db.commit()

# Artists
def create_artist(db: Session, artist: schemas.ArtistCreate):
    db_artist = models.Artist(name=artist.name, genre_id=artist.genre_id)
    db.add(db_artist)
    db.commit()
    db.refresh(db_artist)
    return db_artist

def get_artists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Artist).offset(skip).limit(limit).all()

def get_artist(db: Session, artist_id: int):
    return db.query(models.Artist).filter(models.Artist.id == artist_id).first()

def update_artist(db: Session, artist_id: int, artist: schemas.ArtistCreate):
    db_artist = db.query(models.Artist).filter(models.Artist.id == artist_id).first()
    if db_artist:
        db_artist.name = artist.name
        db_artist.genre_id = artist.genre_id
        db.commit()
        db.refresh(db_artist)
    return db_artist

def delete_artist(db: Session, artist_id: int):
    db_artist = db.query(models.Artist).filter(models.Artist.id == artist_id).first()
    if db_artist:
        db.delete(db_artist)
        db.commit()

# Albums
def create_album(db: Session, album: schemas.AlbumCreate):
    db_album = models.Album(title=album.title, year=album.year, artist_id=album.artist_id)
    db.add(db_album)
    db.commit()
    db.refresh(db_album)
    return db_album

def get_albums(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Album).offset(skip).limit(limit).all()

def get_album(db: Session, album_id: int):
    return db.query(models.Album).filter(models.Album.id == album_id).first()

def update_album(db: Session, album_id: int, album: schemas.AlbumCreate):
    db_album = db.query(models.Album).filter(models.Album.id == album_id).first()
    if db_album:
        db_album.title = album.title
        db_album.year = album.year
        db_album.artist_id = album.artist_id
        db.commit()
        db.refresh(db_album)
    return db_album

def delete_album(db: Session, album_id: int):
    db_album = db.query(models.Album).filter(models.Album.id == album_id).first()
    if db_album:
        db.delete(db_album)
        db.commit()

