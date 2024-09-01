import random

# list of books is stored in the list -'books'
books = ['Tao Te Ching', 'Lessons from a Living Lemuria', 'Art of War', 'Torah', 'The Secret Teaching of All Ages', 'Coraline', 'Cestui Que Vie 1666']

# An item from the list 'books' is selected
# by random.choice()
chosenBook = random.choice(books)

while True:
    print("A door..")
    doorChoice = input("Open - Knock - Do nothing").lower()

    if doorChoice == 'open':
        print("It's locked")
    elif doorChoice == 'knock':
        print("No one answers")
    elif doorChoice == "do nothing":
        print("A whispering voice behind you 'I have your book, don't forget it..'")
        print(chosenBook + "..")
        print("You don't remember?..")
        break
    else:
        print("I didn't understand that.")