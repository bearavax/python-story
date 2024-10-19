import random

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

# Define the story
def start_story():
    print("In the heart of Churchill, where the tundra meets the icy waters of Hudson Bay, lived a polar bear named Nanuq.")
    print("Nanuq, known for his curiosity and gentle spirit, felt a pull towards the human settlement, driven by dreams of a mysterious artifact.")
    print("One crisp morning, as the first snows began to fall, Nanuq encountered a Sayisi Dene elder, Ataata.")
    print("Ataata spoke of an ancient relic, the 'Ice Heart,' believed to be hidden somewhere in Churchill's vicinity.")
    print("This relic, according to legend, could communicate with all creatures, ensuring peace and understanding across species.")
    print("Driven by this tale, Nanuq embarked on his quest, joined by a wise old raven, Kigla, and a spirited Arctic fox, Siku.")
    print("Together, they formed an unlikely trio, each bringing unique skills to their adventure.")
    print()

def make_choice():
    print("What will Nanuq do next?")
    print("1. Seek guidance from the herd of caribou.")
    print("2. Visit the representatives from Polar Bears International.")
    print("3. Explore the tundra with Kigla and Siku.")
    choice = input("Enter the number of your choice: ")
    return choice

def caribou_guidance():
    print("Nanuq, Kigla, and Siku seek guidance from a herd of caribou, led by a majestic bull named Tuktu.")
    print("Tuktu suggests they seek the wisdom of the beluga whales in the Churchill River.")
    print("Amidst the haunting songs of the whales, they learn of a submerged cave where ice never melts, a place untouched by time.")
    print("They now have a clearer path to the Ice Heart.")
    print()

def polar_bears_international():
    print("Nanuq, Kigla, and Siku visit the representatives from Polar Bears International.")
    print("The representatives share data on ice patterns, inadvertently guiding the trio towards an area where the Ice Heart is rumored to be buried under ancient ice.")
    print("They now have a map to guide them on their journey.")
    print()

def explore_tundra():
    print("Nanuq, Kigla, and Siku explore the tundra, encountering various wildlife and collecting useful items.")
    print("They find an ancient relic that might be connected to the Ice Heart.")
    print()

def face_tornaq():
    print("As they venture deeper, they face their greatest challenge yet.")
    print("A rogue polar bear, Tornaq, blocks their way.")
    print("Nanuq engages Tornaq not in battle but in a display of strength and wisdom, showcasing the unity of their group.")
    print("Moved by this display, Tornaq retreats, allowing them passage.")
    print()

def find_ice_heart():
    print("Reaching the cave, they find the Ice Heart, not as a physical object but as a phenomenon.")
    print("The ice resonates with the heartbeat of the Earth itself.")
    print("Nanuq realizes his journey was about becoming a bridge between worlds.")
    print("He understands the messages of the land, the sea, and the sky, and in doing so, he becomes the Ice Heart.")
    print()

def end_story():
    print("Returning to Churchill, Nanuq's presence begins to subtly influence the town.")
    print("Humans and wildlife start to coexist with a newfound respect.")
    print("Polar Bears International documents this change as a case study on coexistence.")
    print("The Sayisi Dene, through Ataata, celebrate Nanuq's journey in their stories, ensuring it will inspire future generations.")
    print("Nanuq, now a legend himself, continues to roam the tundra as a symbol of harmony.")
    print()

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