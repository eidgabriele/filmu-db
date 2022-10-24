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
        pass
    elif selection == "3":
        pprint(read_object(object_class))
        record_id = int(input("Please select record number for deletion:"))
        if record_id:
            delete_object(object_class, record_id)
            print(f"Record id {record_id} was successfully removed from database")
    elif selection == "4":
        pass
    else:
        print("Unavailabe option, try again.")


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
        pass
    elif selection == "3":
        pass
    elif selection == "4":
        pass
    elif selection == "5":
        print("Movie database is closing")
        break
    else:
        print(f"No such option as {selection} was found")