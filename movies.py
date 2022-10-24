from sqlalchemy.orm import sessionmaker
from model import *
from crud import *

session = sessionmaker(engine)()

def choose_crud(object_class):
    print(f"You have selected {object_class.__name__}")
    print(f"Available actions:\n1 - view records,\n2 - add a new record,\n3 - delete record,\n4 - update record")
    selection = str(input("Choose next step: "))
    if selection == "1":
        pprint(read_object(object_class))
    elif selection == "2":
        if object_class == Movie:
            print("filmas")
        elif object_class == Director:
            print("rezisieirus")
        elif object_class == Studio:
            print("studij")


    elif selection == "3":
        pprint(read_object(object_class))
        record_id = int(input("Please select record number for deletion:"))
        if record_id:
            delete_object(object_class, record_id)
            print(f"Record id {record_id} was successfully removed from the database")
    elif selection == "4":
        pass
    else:
        print("Unavailabe option, try again.")

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

while True:
    print(f"--- Movie database ---")
    print(f"1 - Movies")
    print(f"2 - Directors")
    print(f"3 - Studios")
    print(f"5 - Exit application")
    selection = str(input("Choose an option: "))
    if selection == "1":
        choose_crud(Movie)
    elif selection == "2":
        choose_crud(Director)
    elif selection == "3":
        choose_crud(Studio)
    elif selection == "4":
        pass
    elif selection == "5":
        print("Movie database is closing")
        break
    else:
        print(f"No such option as {selection} was found")