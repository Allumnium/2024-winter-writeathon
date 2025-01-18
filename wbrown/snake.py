# Core shamelessly stolen from chatGPT


class TextAdventureGame:
    def __init__(self):
        self.locations = {}
        self.current_location = None
        self.is_playing = True
        self.score = 0
        self.length = 5  # Maximum word length the player can eat
        self.hunger_letter = 'a'  # The letter the player is hungry for

    def add_location(self, name, description, options):
        """
        Add a location to the game.

        Parameters:
        name (str): The name of the location.
        description (str): A brief description of the location.
        options (dict): Actions available in the location. Keys are action names, values are result locations.
        """
        self.locations[name] = {
            "description": description,
            "options": options
        }

    def set_starting_location(self, location_name):
        """Set the starting location of the game."""
        if location_name in self.locations:
            self.current_location = location_name
        else:
            print(f"Error: Location '{location_name}' does not exist.")

    def display_location(self):
        """Display the current location's description and options."""
        location = self.locations[self.current_location]
        print(f"\n{self.current_location}")
        print(location["description"])
        print("\nOptions:")
        for index, option in enumerate(location["options"].keys(), start=1):
            print(f"{index}. {option}")
        print(f"\nScore: {self.score}")
        print(f"Max word length you can eat: {self.length}")
        print(f"You are hungry for words containing: '{self.hunger_letter}'")

    def choose_option(self, choice):
        """Handle the player's choice."""
        location = self.locations[self.current_location]
        options = list(location["options"].keys())

        if isinstance(choice, int) and 0 < choice <= len(options):
            selected_option = options[choice - 1]
            self.current_location = location["options"][selected_option]
            if self.current_location == "END":
                self.is_playing = False
                print("\nThank you for playing!")
        elif isinstance(choice, str):
            description_words = location["description"].split()
            if choice in description_words and len(choice) <= self.length:
                print(f"You eat the word: {choice}")
                if self.hunger_letter in choice:
                    points = len(choice)
                    self.score += points
                    print(f"The word contains '{self.hunger_letter}'. You gain {points} points!")
                description_words.remove(choice)
                location["description"] = " ".join(description_words)
            elif choice in description_words:
                print(f"The word '{choice}' is too long to eat.")
            else:
                print("Invalid word. Please try again.")
        else:
            print("Invalid choice. Please try again.")

    def start(self):
        """Start the game loop."""
        while self.is_playing:
            self.display_location()
            try:
                user_input = input("\nEnter your choice: ")
                if user_input.isdigit():
                    choice = int(user_input)
                else:
                    choice = user_input
                self.choose_option(choice)
            except ValueError:
                print("Invalid input. Please enter a valid option.")

# My crap will eventually go below
if __name__ == "__main__":
    game = TextAdventureGame()

    # Define locations
    game.add_location(
        "Forest Entrance",
        "You are standing at the edge of a dark forest. Paths lead north and east. There is also a signpost.",
        {"Go North": "Dark Clearing", "Go East": "Abandoned Cabin", "Read Signpost": "Signpost Area"}
    )

    game.add_location(
        "Dark Clearing",
        "You find yourself in a clearing shrouded in mist. You hear a distant howl.",
        {"Return South": "Forest Entrance", "Investigate the Howl": "END"}
    )

    game.add_location(
        "Abandoned Cabin",
        "The cabin is old and decrepit, with its door hanging ajar.",
        {"Return West": "Forest Entrance", "Enter the Cabin": "END"}
    )

    game.add_location(
        "Signpost Area",
        "The signpost has faded writing. You can try to decipher it.",
        {"Enter String": "Forest Entrance"}
    )

    # Set starting location
    game.set_starting_location("Forest Entrance")

    # Start the game
    game.start()

