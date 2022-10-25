from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from model import *
from crud import *

session = sessionmaker(engine)()

def choose_crud(object_class):
    print(f"You have selected {object_class.__name__}")
    print(f"Available actions:\n1 - view records,\n2 - add a new record,\n3 - delete record,\n4 - add genre to movie,\n5 - add studio to movie\n6 - add director to movie")
    selection = str(input("Choose next step: "))
    if selection == "1":
        pprint(read_object(object_class))
        if object_class == Movie:
            movie_detailed()
        if object_class == Director:
            director_detailed()
    elif selection == "2":
        if object_class == Movie:
            add_movie()
        elif object_class == Director:
            add_director()
        elif object_class == Studio:
            add_studio()
    elif selection == "3":
        pprint(read_object(object_class))
        record_id = int(input("Please select record number for deletion:"))
        if record_id:
            delete_object(object_class, record_id)
            print(f"Record id {record_id} was successfully removed from the database")
    elif object_class == Movie and selection == "4":
        add_genre()
    elif object_class == Movie and selection == "5":
        add_movie_studio()
    elif object_class == Director and selection == "6":
        add_movie_director()
    else:
        print("Unavailabe option, try again.")

def movie_detailed():
    pprint(read_object(Movie))
    print("---Enter movie id for detailed information---")
    try:
        movie_id = int(input("Movie id: "))
    except ValueError:
        print("Error, bad input")
    else:
        if movie_id:
            selected_movie = session.query(Movie).get(movie_id)
            print("----MOVIE INFORMATION----")
            print(f"Movie name: {selected_movie.name}")
            print(f"Release year: {selected_movie.release_year}")
            print(f"Budget: {selected_movie.budget}$")
            print(f"Runtime: {selected_movie.runtime} minutes")
            print(f"Rating: {selected_movie.rating}")
            print(f"Director: {selected_movie.director.name} {selected_movie.director.surname}")
            print("Genres:")
            for genre in selected_movie.movie_genres:
                print(f" - {genre.genres.name}")
            print("Studios:")
            for studio in selected_movie.movie_studios:
                print(f" - {studio.studios.name}")

def director_detailed():
    pprint(read_object(Director))
    print("---Enter director id for detailed information---")
    try:
        director_id = int(input("Director id: "))
    except ValueError:
        print("Error, bad input")
    else:
        selected_director = session.query(Director).get(director_id)
        print("----DIRECTOR INFORMATION----")
        print(f"Name: {selected_director.name}")
        print(f"Surname: {selected_director.surname}")
        print(f"Directed movies:")
        for movie in selected_director.movies:
            print(f"  {movie.name} ({movie.release_year}), budget {movie.budget}$")



def add_movie_director():
    print("---Enter movie id to add/edit director---")
    try:
        pprint(read_object(Movie))
        movie_id = int(input("Movie id: "))
        print("Select director id from the following:")
        pprint(read_object(Director))
        director_id = int(input("Director id: "))
    except ValueError:
        print("Error, bad input")
    else:
        update_object(Movie, movie_id, director_id = director_id)
        print(f"Director id {director_id} was added to movie id {movie_id}")
        selected_movie = session.query(Movie).get(movie_id)
        print(f"Name: {selected_movie.name} ({selected_movie.release_year})")
        print(f"Director: {selected_movie.director.name} {selected_movie.director.surname}")



def add_movie_studio():
    print("---Enter movie id to add studios---")
    try:
        movie_id = int(input("Movie id: "))
        pprint(read_object(Studio))
        studio_id = int(input("Studio id:"))
    except ValueError:
        print("Error, bad input")
    else:
        if movie_id and studio_id:
            create_object(Movie_studio, studio_id = studio_id, movie_id = movie_id)
            print(f"Studio {session.query(Studio).get(studio_id)} was added successfully to movie {session.query(Movie).get(movie_id).name}")

def add_genre():
    print("---Enter movie id to add genres---")
    try:
        movie_id = int(input("Movie id: "))
        pprint(read_object(Genre))
        genre_id = int(input("Genre id:"))
    except ValueError:
        print("Error, bad input")
    else:
        if movie_id and genre_id:
            create_object(Movie_genre, genre_id = genre_id, movie_id = movie_id)
            print(f"Genre {session.query(Genre).get(genre_id)} was added successfully to movie {session.query(Movie).get(movie_id).name}")


def add_movie():
    print("---Adding new movie---")
    try:
        name = input("Name: ")
        release_year = int(input("Release year: "))
        budget = float(input("Budget: "))
        runtime = int(input("Runtime: "))
        rating = float(input("Rating: "))
        director_id = int(input("Director (id from list): "))
    except ValueError:
        print("Wrong input")
    else:
        new_movie = create_object(Movie, name = name, release_year = release_year, budget = budget, runtime = runtime, rating = rating, director_id = director_id)
        print(f"Movie {name} was added successfully to the database")

def add_director():
    print("---Adding new director---")
    try:
        name = input("Name: ")
        surname = input("Surname: ")
    except ValueError:
        print("Wrong input")
    else:
        new_director = create_object(Director, name = name, surname = surname)
        print(f"Director {name} {surname} was added successfully to the database")

def add_studio():
    print("---Adding new studio---")
    try:
        name = input("Name: ")
        country = input("Country: ")
    except ValueError:
        print("Wrong input")
    else: 
        new_studio = create_object(Studio, name = name, country = country)
        print(f"Studio {name} was added successfully to the database")

def statistics():
    print("---Movie database stats---")
    print("Total records: ")
    print(f"Movies: {session.query(Movie).count()}")
    print(f"Directors: {session.query(Director).count()}")
    print(f"Studios: {session.query(Studio).count()}")
    with engine.connect() as conn:
        oldest = conn.exec_driver_sql('SELECT * FROM Movie ORDER BY release_year ASC LIMIT 3')
        print(f"Oldest movies:")
        for old in oldest:
            print(f"   ◉  {old.name} ({old.release_year})")
        longest = conn.exec_driver_sql('SELECT * FROM Movie ORDER BY runtime DESC LIMIT 3')
        print(f"The longest movies:")
        for long in longest:
            print(f"   ◉  {long.name} - {long.runtime} minutes")
        most_expensive = conn.exec_driver_sql('SELECT * FROM Movie ORDER BY budget DESC LIMIT 3')
        print(f"The most expensive movies:")
        for expensive in most_expensive:
            print(f"   ◉  {expensive.name} - {expensive.budget}$")
            

        
    

while True:
    print(f"--- Movie database ---")
    print(f"1 - Movies")
    print(f"2 - Directors")
    print(f"3 - Studios")
    print(f"4 - Statistics")
    print(f"5 - Exit application")
    selection = str(input("Choose an option: "))
    if selection == "1":
        choose_crud(Movie)
    elif selection == "2":
        choose_crud(Director)
    elif selection == "3":
        choose_crud(Studio)
    elif selection == "4":
        statistics()
    elif selection == "5":
        print("Movie database is closing")
        break
    else:
        print(f"No such option as {selection} was found")