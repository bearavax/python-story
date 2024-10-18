import random

print("It's a snowstorm in the tundra. You are all alone.")

while True:
    choice = input("Press 1 to shuffle..")
    if choice == "1":
        print("Shuffle, shuffle")
        break
    else:
        print("Try again.")
        
print(".. ... ..")

print("hello")

inventory = 0

while True:
    choice = input("Press 1 to start mining or 2 to stop mining: ")
    if choice == "1":
        rocks = random.randint(1, 10)
        inventory += rocks
        print(f"You mined {rocks} rocks. Total inventory: {inventory}")
    elif choice == "2":
        print(f"You stopped mining. Final inventory: {inventory} rocks.")
        break
    else:
        print("Invalid choice. Try again.")