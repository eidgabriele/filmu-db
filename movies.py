from sqlalchemy.orm import sessionmaker
from model import *
from crud import *

session = sessionmaker(engine)()

while True:
    print(f"--- Movie database ---")
    print(f"1 - Movies")
    print(f"2 - Directors")
    print(f"3 - Studios")
    print(f"5 - Exit application")
    selection = str(input("Choose an option: "))
    if selection == "1":
        pass
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