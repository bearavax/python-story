import random
import json

# Define the characters and items
characters = {
    "Nanuq": {"type": "polar bear", "description": "A curious and gentle polar bear."},
    "Ataata": {"type": "Sayisi Dene elder", "description": "A wise elder who knows about the Ice Heart."},
    "Kigla": {"type": "raven", "description": "A wise old raven who knows the tundra's secrets."},
    "Siku": {"type": "Arctic fox", "description": "A spirited Arctic fox with unmatched agility and wit."},
    "Tuktu": {"type": "caribou", "description": "A majestic bull caribou who offers guidance."},
    "Tornaq": {"type": "rogue polar bear", "description": "A ferocious bear driven mad by hunger."}
}

items = {
    "Ice Heart": {"description": "A phenomenon where the ice resonates with the heartbeat of the Earth."},
    "Map": {"description": "A map showing the ice patterns and guiding towards the Ice Heart."},
    "Ancient Relic": {"description": "An ancient relic believed to bring harmony between humans and wildlife."}
}

inventory = []
health = 100

def start_story():
    print("In the heart of Churchill, lived a polar bear named Nanuq.")
    print("Driven by dreams of a mysterious artifact, Nanuq felt a pull towards the human settlement.")
    print("One morning, Nanuq encountered Ataata, a Sayisi Dene elder.")
    print("Ataata spoke of the 'Ice Heart,' believed to be hidden nearby.")
    print("Joined by Kigla the raven and Siku the Arctic fox, Nanuq embarked on a quest.")
    print()

def make_choice():
    print("What will Nanuq do next?")
    print("1. Seek guidance from the caribou.")
    print("2. Visit Polar Bears International.")
    print("3. Explore the tundra.")
    choice = input("Enter the number of your choice: ")
    return choice

def caribou_guidance():
    print("Nanuq, Kigla, and Siku seek guidance from Tuktu, the caribou.")
    print("Tuktu suggests seeking the wisdom of the beluga whales.")
    print("They learn of a submerged cave where ice never melts.")
    collect_item("Map")

def polar_bears_international():
    print("Nanuq, Kigla, and Siku visit Polar Bears International.")
    print("They share data on ice patterns, guiding the trio towards the Ice Heart.")
    collect_item("Map")

def explore_tundra():
    print("Nanuq, Kigla, and Siku explore the tundra.")
    print("They find an ancient relic connected to the Ice Heart.")
    collect_item("Ancient Relic")

def face_tornaq():
    print("A rogue polar bear, Tornaq, blocks their way.")
    print("Nanuq engages Tornaq in a display of strength and wisdom.")
    print("Tornaq retreats, allowing them passage.")
    take_damage(20)

def find_ice_heart():
    print("Reaching the cave, they find the Ice Heart.")
    print("The ice resonates with the heartbeat of the Earth.")
    print("Nanuq becomes the bridge between worlds.")
    collect_item("Ice Heart")

def end_story():
    print("Returning to Churchill, Nanuq's presence influences the town.")
    print("Humans and wildlife start to coexist with respect.")
    print("Nanuq, now a legend, continues to roam the tundra as a symbol of harmony.")
    print()

def collect_item(item):
    inventory.append(item)
    print(f"You have collected: {item}")

def take_damage(amount):
    global health
    health -= amount
    print(f"You took {amount} damage. Your health is now {health}.")
    if health <= 0:
        print("You have perished in the tundra.")
        exit()

def save_game(filename="savegame.json"):
    game_state = {
        "inventory": inventory,
        "health": health
    }
    with open(filename, "w") as file:
        json.dump(game_state, file)
    print("Game saved.")

def load_game(filename="savegame.json"):
    global inventory, health
    with open(filename, "r") as file:
        game_state = json.load(file)
    inventory = game_state["inventory"]
    health = game_state["health"]
    print("Game loaded.")

# Main function to run the story
def main():
    start_story()
    while True:
        choice = make_choice()
        if choice == "1":
            caribou_guidance()
        elif choice == "2":
            polar_bears_international()
        elif choice == "3":
            explore_tundra()
        else:
            print("Invalid choice. Please try again.")
            continue
        
        face_tornaq()
        find_ice_heart()
        end_story()
        break

if __name__ == "__main__":
    main()