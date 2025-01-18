# Core shamelessly stolen from chatGPT
class TextAdventureGame:
    def __init__(self):
        self.locations = {}
        self.current_location = None
        self.is_playing = True

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

    def choose_option(self, choice):
        """Handle the player's choice."""
        location = self.locations[self.current_location]
        options = list(location["options"].keys())

        if 0 < choice <= len(options):
            selected_option = options[choice - 1]
            self.current_location = location["options"][selected_option]
            if self.current_location == "END":
                self.is_playing = False
                print("\nThank you for playing!")
        else:
            print("Invalid choice. Please try again.")

    def start(self):
        """Start the game loop."""
        while self.is_playing:
            self.display_location()
            try:
                choice = int(input("\nEnter your choice: "))
                self.choose_option(choice)
            except ValueError:
                print("Invalid input. Please enter a number.")

# My crap will eventually go below
if __name__ == "__main__":
    game = TextAdventureGame()

    # Define locations
    game.add_location(
            ""
        "Forest Entrance",
        "You are standing at the edge of a dark forest. Paths lead north and east.",
        {"Go North": "Dark Clearing", "Go East": "Abandoned Cabin"}
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

    # Set starting location
    game.set_starting_location("Forest Entrance")

    # Start the game
    game.start()

