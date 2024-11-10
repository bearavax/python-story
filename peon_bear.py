import random

class PolarBear:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.rocks = 0
        self.supplies = 0

    def smash(self):
        rocks_found = random.randint(1, 5)
        self.rocks += rocks_found
        print(f"{self.name} smashed and found {rocks_found} rocks! Total rocks: {self.rocks}")

    def rest(self):
        self.health += 10
        if self.health > 100:
            self.health = 100
        print(f"{self.name} rests and recovers health. Current health: {self.health}")

    def trade(self):
        if self.rocks >= 5:
            self.rocks -= 5
            self.supplies += 1
            print(f"{self.name} traded 5 rocks for 1 supply. Total supplies: {self.supplies}")
        else:
            print(f"Not enough rocks to trade. {self.name} needs 5 rocks to trade.")

    def status(self):
        print(f"{self.name}'s Status - Health: {self.health}, Rocks: {self.rocks}, Supplies: {self.supplies}")

def main():
    print("Welcome to the Deep Shaft Mining Adventure!")
    name = input("Enter the name of your polar bear: ")
    bear = PolarBear(name)

    while True:
        print("\nChoose an action:")
        print("1. Smash (mine for supplies)")
        print("2. Rest (recover health)")
        print("3. Trade (trade rocks for supplies)")
        print("4. Status (check status)")
        print("5. Quit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            bear.smash()
        elif choice == "2":
            bear.rest()
        elif choice == "3":
            bear.trade()
        elif choice == "4":
            bear.status()
        elif choice == "5":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()