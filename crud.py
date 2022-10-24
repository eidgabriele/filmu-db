from sqlalchemy.orm import sessionmaker
from model import engine, Movie, Director, Genre, Studio, Movie_genre, Movie_studio

session = sessionmaker(bind=engine)()

def create_object(object_class, **kwargs):
    obj = object_class(**kwargs)
    session.add(obj)
    session.commit()
    return obj

def read_object(object_class):
    obj = session.query(object_class).all()
    return obj

if __name__ == "__main__":
    create_object(Movie, name = "Whiplash", release_year =2014, budget = 3300000,  runtime = 106, rating  = 8.5, director_id = 1)
    # zanras = create_object(Genre, name="comedy")
    # studija = create_object(Studio, name = "Paramount Pictures")
    print(read_object(Studio))
    print(read_object(Movie))
