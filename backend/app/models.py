from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    artists = relationship("Artist", back_populates="genre", cascade="all, delete")

class Artist(Base):
    __tablename__ = "artists"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    genre_id = Column(Integer, ForeignKey("genres.id"))
    genre = relationship("Genre", back_populates="artists")
    albums = relationship("Album", back_populates="artist", cascade="all, delete")

class Album(Base):
    __tablename__ = "albums"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    year = Column(Integer, nullable=True)
    artist_id = Column(Integer, ForeignKey("artists.id"))
    artist = relationship("Artist", back_populates="albums")
