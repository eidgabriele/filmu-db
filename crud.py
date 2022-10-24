from sqlalchemy.orm import sessionmaker
from model import engine, Movie, Director, Genre, Studio, Movie_genre, Movie_studio
from pprint import pprint

session = sessionmaker(bind=engine)()

def create_object(object_class, **kwargs):
    obj = object_class(**kwargs)
    session.add(obj)
    session.commit()
    return obj

def read_object(object_class):
    obj = session.query(object_class).all()
    return obj

def delete_object(object_class, object_id):
    obj = session.query(object_class).get(object_id)
    if obj:
        session.delete(obj)
        session.commit()
        return True
    else:
        print(f"Error: {object_class.__name__} object ID:{object_id} not found")

def update_object(object_class, object_id, **kwargs):
    obj = session.query(object_class).get(object_id)
    if obj and kwargs:
        for column_name, value in kwargs.items():
            if hasattr(obj, column_name):
                setattr(obj, column_name, value)
            else:
                print(f"Error: {obj} has no {column_name} attribute")
        else:
            session.commit()
            return obj
    else:
        print(f"Error: {object_class.__name__} object ID:{object_id} not found")

if __name__ == "__main__":
    # create_object(Movie, name = "Marie Antoinette", release_year =2006, budget = 40000000 , runtime =123, rating = 6.5, director_id =11)
    # print(read_object(Studio))
    pprint(read_object(Genre))
    pprint(read_object(Movie))
    # print(read_object(Director))
    # delete_object(Director, 5)
    pprint(read_object(Director))
    # update_object(Studio, 2, country = "USA")
    pprint(read_object(Studio))
    # create_object(Movie_genre, genre_id = 6, movie_id = 30)