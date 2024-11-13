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

class Peon:
    def __init__(self, name):
        self.name = name
        self.health = 50

    def work(self):
        work_done = random.randint(1, 3)
        print(f"{self.name} worked and contributed {work_done} rocks.")
        return work_done

    def rest(self):
        self.health += 5
        if self.health > 50:
            self.health = 50
        print(f"{self.name} rests and recovers health. Current health: {self.health}")

def main():
    print("Welcome to the Deep Shaft Mining Adventure!")
    print("In the icy depths of the tundra, a polar bear named Nanuq leads a group of peons in search of precious supplies.")
    name = input("Enter the name of your polar bear: ")
    bear = PolarBear(name)

    peons = [Peon("Peon1"), Peon("Peon2"), Peon("Peon3")]

    while True:
        print("\nChoose an action:")
        print("1. Smash (mine for supplies)")
        print("2. Rest (recover health)")
        print("3. Trade (trade rocks for supplies)")
        print("4. Status (check status)")
        print("5. Command Peons (assign tasks to peons)")
        print("6. Quit")

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
            print("Choose a peon to command:")
            for i, peon in enumerate(peons):
                print(f"{i + 1}. {peon.name} (Health: {peon.health})")
            peon_choice = int(input("Enter the number of your choice: ")) - 1
            if 0 <= peon_choice < len(peons):
                peon = peons[peon_choice]
                print(f"1. Make {peon.name} work")
                print(f"2. Make {peon.name} rest")
                peon_action = input("Enter the number of your choice: ")
                if peon_action == "1":
                    rocks_contributed = peon.work()
                    bear.rocks += rocks_contributed
                elif peon_action == "2":
                    peon.rest()
                else:
                    print("Invalid choice. Please try again.")
            else:
                print("Invalid choice. Please try again.")
        elif choice == "6":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()