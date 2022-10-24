from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///data/movies.db')
Base = declarative_base()

class Director(Base):
    __tablename__ = "director"
    id = Column(Integer, primary_key = True)
    name = Column("name", String)
    surname = Column("surname", String)
    movies = relationship("Movie", back_populates="director")

    def __repr__(self):
        return f"{self.id}, {self.name}, {self.surname}"

class Genre(Base):
    __tablename__ = "genre"
    id = Column(Integer, primary_key = True)
    name = Column("name", String)
    movie_genres = relationship("Movie_genre", back_populates = 'genres')

    def __repr__(self):
        return f"{self.id}, {self.name}"

class Studio(Base):
    __tablename__ = "studio"
    id = Column(Integer, primary_key = True)
    name = Column("name", String)
    country = Column("country", String)
    movie_studio = relationship("Movie_studio", back_populates = 'studios')

    def __repr__(self):
        return f"{self.id}, {self.name}, {self.country}"

class Movie(Base):
    __tablename__ = "movie"
    id = Column(Integer, primary_key = True)
    name = Column("name", String)
    release_year = Column("release_year", Integer)
    budget = Column("budget", Float)
    runtime = Column("runtime", Integer)
    rating = Column("rating", Float)
    director = relationship("Director", back_populates = "movies")
    director_id = Column(Integer, ForeignKey('director.id'))
    movie_genres = relationship("Movie_genre", back_populates = "movies")
    movie_studios = relationship("Movie_studio", back_populates = "movies")

    def __repr__(self):
        return f"{self.id}, {self.name}, {self.release_year}, {self.runtime}"

    
class Movie_genre(Base):
    __tablename__ = "movie_genre"
    id = Column(Integer, primary_key= True)
    genres = relationship("Genre", back_populates = "movie_genres")
    genre_id = Column(Integer, ForeignKey('genre.id'))
    movies = relationship("Movie", back_populates = "movie_genres")
    movie_id = Column(Integer, ForeignKey('movie.id'))

    def __repr__(self):
        return f"{self.id}, {self.genre_id}, {self.movie_id}"

class Movie_studio(Base):
    __tablename__ = "movie_studio"
    id = Column(Integer, primary_key= True)
    studios = relationship("Studio", back_populates = "movie_studios")
    studio_id = Column(Integer, ForeignKey('studio.id'))
    movies = relationship("Movie", back_populates = "movie_studios")
    movie_id = Column(Integer, ForeignKey('movie.id'))

    def __repr__(self):
        return f"{self.id}, {self.studio_id}, {self.movie_id}"



if __name__ == "__main__":
    Base.metadata.create_all(engine)