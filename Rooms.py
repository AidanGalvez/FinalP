import pickle
class Room:
    def __init__(self, name, description, items = []):
        self.__name = name
        self.__description = description
    
    def __str__(self):
        return f"\n\nLocation: {self.__name}\n{self.__description}\n\n"

class Inventory:
    def __init__(self):
        self.__items = []
    
    def add_item(self, item):
        self.__items.append(item)
    
    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
    
    def show_inventory(self):
        if len(self.__items) == 0:
            print("\nYour inventory is empty.")
        else:
            print("\nYour inventory contains:")
            for item in self.__items:
                print("- " + item)
            return self.__items
    
    def __iter__(self):
        return iter(self.__items)
        
class Player:
    def __init__(self, starting_room, clockcount):
        self.current_room = starting_room
        self.inventory = Inventory()
        self.clockcount = []
        self.item_grabbed = []
        self.item_used = []
    
    def playerchoice(self):
        player_quit = False
        choice = input("What would you like to do?\n").lower()
        while choice not in ["up", "down", "left", "right", "forward", "back", "grab", "use", "save", "load", "quit", "inventory", "controls"]:
            print(f'"{choice}" is not a valid option\n')
            choice = input("\nWhat would you like to do?\n").lower()
        if choice == "inventory":
            self.inventory.show_inventory()
            print()
        if choice == "use":
            self.use_item()
        if choice == "grab":
            self.grab_item()
        if choice == "save":
            self.save_game()
        if choice == "load":
            self.load_game()
        if choice == "quit":
            player_quit = True
        if choice == "controls":
            print(f"\nControls: up, down, left, right, forward, back, grab, use, save, load, quit, inventory, and controls\nObjective: Collect all 10 clocks and escape school\nTotal clocks collected: {len(self.clockcount)}")
            print("|Clocks collected|")
            for clock in self.clockcount:
                print(f"•{clock}")
            print()
        if choice == "back" and self.current_room == "Outside":
            print("\n\nYou try making a run for your car however a teacher stops you and drags you back inside.")  
        if choice == "forward" and self.current_room == "Outside2":
            if f"Outside clock" not in self.clockcount:
                print("\n\nYou try running away on the second floor hoping no one would see you and while you were running you found a clock, however someone driving in a golf cart found you and threw you back inside")
                self.clockcount.append("Outside clock")
                print(f"\nYou have collected the Outside clock!\n")
            else:
                print("\n\nYou try running away on the second floor hoping no one would see you, however someone driving in a golf cart found you and threw you back inside")
        return choice, player_quit

    def save_game(self):
        save_data = {
            "current_room": self.current_room,
            "clockcount": self.clockcount,
            "inventory": self.inventory
        }
        filename = 'game_saved'

        with open(filename, 'wb') as file:
            pickle.dump(save_data, file)

        print(f"Game saved as '{filename}'.")

    def load_game(self):
        filename = 'game_saved'

        try:
            with open(filename, 'rb') as file:
                save_data = pickle.load(file)

            player = Player(save_data["current_room"], save_data["clockcount"])
            loaded_player = Player(save_data["current_room"], save_data["clockcount"])
            self.current_room = loaded_player.current_room
            self.clockcount = loaded_player.clockcount
            self.inventory = loaded_player.inventory

            self.clockcount = save_data["clockcount"]
            self.inventory = save_data["inventory"]

            print(f"Game loaded from '{filename}'.")
            print(self.clockcount)
            return loaded_player

        except FileNotFoundError:
            print("No saved game file found.")
            return None
    
    def use_item(self):
        if self.current_room == "Store":
            if "Money" in self.inventory and "Money" not in self.item_used:
                self.inventory.remove_item("Money")
                self.item_used.append("Money")
                print("\nmoney has been removed from your inventory\nGummies have been added to your inventory\n")
                self.inventory.add_item("Gummies")
            elif "Money" in self.item_used:
                print("\nYou already bought the gummies\n")
            else:
                print("\nYou don't have any money to buy the gummies\n")

        elif self.current_room == "Gym":
            if "Water bottle" in self.inventory:
                self.inventory.remove_item("Water bottle")
                print("\nYou gave the water bottle to the person working out\nThey jumped up and grabbed you the clock as an appreciation")
                self.clockcount.append(f"{self.current_room} clock")
                print()
            else:
                print("\nThe person looks thirsty maybe you should bring them some water?\n")

        elif self.current_room == "Science":
            if "Towel" in self.inventory:
                self.inventory.remove_item("Towel")
                self.item_used.append("Towel")
                print("\nYou have cleaned the chemicals off the clock, would you like to grab the clock?\n")

        elif self.current_room == "ThirdFloorRH":
            if "Gummies" not in self.item_grabbed:
                self.inventory.remove_item("Gummies")
                self.item_grabbed.append("Gummies")
                self.clockcount.append(f"Bully clock")
                print("\nYou give the bully the gummies and in return he gives you a clock he stole.\n")
                print(f"\nYou have collected the Bully clock!\n")
            else:
                print("\nYou don't have the gummies he wants, better leave before he decides to fight.\n")

        elif self.current_room == "Office":
            if "Physical Ticket" in self.inventory and "Science Ticket" in self.inventory and "English Ticket" in self.inventory and "Math Ticket" in self.inventory:
                self.inventory.remove_item("Physical Ticket")
                self.inventory.remove_item("Science Ticket")
                self.inventory.remove_item("English Ticket")
                self.inventory.remove_item("Math Ticket")
                print("\nYou traded all your tickets in for a battery\n")
                self.inventory.add_item("battery")
            else:
                print("\nYou don't have all the tickets required\n")

        else:
            print("\nThere is nothing to use in this room\n")
        
        if "battery" in self.inventory and "Dead clock" in self.inventory:
            self.inventory.show_inventory()
            combine = input("\nWould you like to use the battery on the dead clock?\n")
            if combine == "use":
                print("\nYou put the battery into the dead clock and it starts ticking\n")
                self.inventory.remove_item("battery")
                self.inventory.remove_item("Dead clock")
                self.clockcount.append("Roof clock")
            else:
                None

    def grab_item(self):
        if self.current_room == "Physical" or self.current_room == "English" or self.current_room == "Office" or self.current_room == "Math" or self.current_room == "Store":
            if f"{self.current_room} clock" not in self.clockcount:
                self.clockcount.append(f"{self.current_room} clock")
                print(f"\nYou have collected the {self.current_room} clock!\n")
            else:
                print(f"\nYou have already colleced the {self.current_room} clock\n")

        elif self.current_room == "Science" and "Towel" not in self.item_used:
                print("\nThe clock is covered in chemicals and probably dangerous to touch, you should find something to clean it off with.\n")
        elif self.current_room == "Science" and "Towel" in self.item_used:
            if f"{self.current_room} clock" not in self.clockcount:
                self.clockcount.append(f"{self.current_room} clock")
                print(f"\nYou have collected the {self.current_room} clock!\n")
            else:
                print(f"\nYou have already colleced the {self.current_room} clock\n")
        
        elif self.current_room == "Gym":
            print("\nThere is a clock that you can grab however it is to high to reach, maybe someone can grab it for you\n")

        elif self.current_room == "Janitor":
            if "Towel" not in self.item_grabbed:
                print("\nYou have grabbed a towel\n")
                self.inventory.add_item("Towel")
                self.item_grabbed.append("Towel")
            else:
                print("\nYou already got the towel\n")

        elif self.current_room == "RoofP2":
            if "Dead clock" not in self.item_grabbed:
                print("\nYou have grabbed a a clock, however it seems that it is dead\n")
                self.inventory.add_item("Dead clock")
                self.item_grabbed.append("Dead clock")
            else:
                print("\nYou already got the Dead clock\n")

        elif self.current_room == "Cafeteria":
            if "Water bottle" not in self.item_grabbed:
                self.inventory.add_item("Water bottle")
                self.item_grabbed.append("Water bottle")
                print("\nYou have grabbed a Water bottle!\n")
            else:
                print("\nYou already got the water bottle\n")
        
        elif self.current_room == "SecondFloorLH":
            if "Money" not in self.item_grabbed:
                self.inventory.add_item("Money")
                self.item_grabbed.append("Money")
                print("\nYou walked up to the plant and you realize it's leaves are made of cash. I guess money really does grow on trees.\n")
            else:
                print("\nYou already got the money from the tree\n")
        else:
            print("\nThere is nothing to grab in here\n")
        
    def move(self, direction):
        connections = {
            "Outside": {"forward": "MainArea", "back": "MainArea"},
            "MainArea": {"back": "Outside", "left": "Store", "right": "Gym", "forward": "Cafeteria"},
            "Cafeteria": {"left": "Store", "right": "Stairs", "back": "MainArea"},
            "Store": {"back": "Cafeteria"},
            "Gym": {"left": "MainArea", "forward": "Physical"},
            "English": {"forward": "ThirdFloorLH"},
            "Stairs": {"up": "SecondFloor", "left": "Cafeteria"},
            "Stairs2": {"up": "ThirdFloor", "down": "Cafeteria", "left": "SecondFloorP2"},
            "Stairs3": {"down": "SecondFloor", "left": "ThirdFloorP2"},
            "SecondFloor": {"left": "SecondFloorLH", "right": "SecondFloorRH", "forward": "SecondFloorP2"},
            "SecondFloorP2": {"forward": "Outside2", "right": "Stairs2", "back": "SecondFloor"},
            "Outside2": {"back": "SecondFloorP2", "forward" : "SecondFloorP2"},
            "Math": {"forward": "SecondFloorRH"},
            "Science": {"back": "SecondFloorLH"},
            "ThirdFloor": {"left": "ThirdFloorLH", "right": "ThirdFloorRH", "forward": "ThirdFloorP2"},
            "ThirdFloorP2":{"left": "Office", "right": "Stairs3", "back" : "ThirdFloor"},
            "Ladder": {"up": "Roof", "back": "ThirdFloorRH"},
            "Office": {"right": "ThirdFloorP2"},
            "Physical": {"back": "Gym"},
            "Roof": {"down": "ThirdFloorRH", "left": "RoofP2"},
            "RoofP2": {"right": "Roof"},
            "SecondFloorLH": {"forward": "Science", "right": "SecondFloor"},
            "SecondFloorRH": {"back": "Math", "left": "SecondFloor"},
            "ThirdFloorRH": {"forward": "Ladder", "left": "ThirdFloor", "back": "Janitor"},
            "Janitor": {"forward": "ThirdFloorRH"},
            "ThirdFloorLH": {"back": "English", "right": "ThirdFloor"},
        
        }
    
        if direction not in connections[self.current_room]:
            if direction not in ["use", "grab", "inventory", "controls", "save", "load", "quit"]:
                print("\nYou cannot go that direction\n")
            return 
        self.current_room = connections[self.current_room][direction]
        locations = ["MainArea", "Outside", "Store", "Gym", "Cafeteria", "English", "Stairs", "Stairs2", "Stairs3",
                    "SecondFloor", "SecondFloorP2", "Outside2", "Math", "Science", "ThirdFloor", "ThirdFloorP2",
                    "Ladder", "Office", "Physical", "Roof", "RoofP2", "SecondFloorLH", "SecondFloorRH", "ThirdFloorRH", "Janitor", "ThirdFloorLH"]
        if self.current_room in locations:
            print(eval(self.current_room))
            if self.current_room == "Physical" and "Physical Ticket" not in self.item_grabbed:
                physical_teacher = Teacher("Mr. Strong", "Physical")
                ticket = physical_teacher.ask_question()
                if ticket:
                    self.inventory.add_item(ticket)
                    self.item_grabbed.append(ticket)
                    print(f"\nYou have collected the {ticket}!\n")
            elif self.current_room == "English" and "English Ticket" not in self.item_grabbed:
                english_teacher = Teacher("Mr. Beakholt", "English")
                ticket = english_teacher.ask_question()
                if ticket:
                    self.inventory.add_item(ticket)
                    self.item_grabbed.append(ticket)
                    print(f"\nYou have collected the {ticket}!\n")
            elif self.current_room == "Math" and "Math Ticket" not in self.item_grabbed:
                math_teacher = Teacher("Mrs. S", "Math")
                ticket = math_teacher.ask_question()
                if ticket:
                    self.inventory.add_item(ticket)
                    self.item_grabbed.append(ticket)
                    print(f"\nYou have collected the {ticket}!\n")
            elif self.current_room == "Science" and "Science Ticket" not in self.item_grabbed:
                science_teacher = Teacher("Mrs. T", "Science")
                ticket = science_teacher.ask_question()
                if ticket:
                    self.inventory.add_item(ticket)
                    self.item_grabbed.append(ticket)
                    print(f"\nYou have collected the {ticket}!\n")
        else:
            print("broken")

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.inventory = Inventory()

    def ask_question(self):
        if self.subject == "Math":
            question = f"{self.name} asks: What is 9 + 3?\n"
            correct_answer = "12"
        elif self.subject == "Science":
            question = f"{self.name} asks: What is the color of the sky?\n"
            correct_answer = "blue"
        elif self.subject == "English":
            question = f"{self.name} asks: What is the correct form of there/they're/their as it is used in this sentence. That is ____ candy that they stole from the superstore.\n"
            correct_answer = "their"
        elif self.subject == "Physical":
            question = f"{self.name} asks: how many holes does a bowling ball have?\n"
            correct_answer = "3"
        else:
            question = f"{self.name} asks: Answer\n"
            correct_answer = ""

        while True:
            answer = input(question)
            if answer.lower() == correct_answer.lower():
                print("Correct!")
                return f"{self.subject} Ticket"
                break
            else:
                print("Incorrect! Try again.")


# rooms and definitions
Outside = Room("Outside", "You are outside of school looking up at the building regretting showing up, you can go into the school or try to leave.")
MainArea = Room("MainArea", "You are in the main area, there are lunch tables with people working in the cafeteria in front of you. You can see the stairs to the right of cafeteria. You see a store to your left that sells various items that may help you get through the day. To your right you can see the gym.")
Store = Room("Store", "There is mostly junk in here but they do have gummies you can buy. You see a clock on the wall out of the corner of your eye.")
Gym = Room("Gym", "You enter the gym which is full of equipment and there is someone doing calf raises in the corner, they look thirsty. You also see your first period class P.E. in front of you. The main area is to your left.")
English = Room("English class", "You enter your English class where the teacher is reciting Shakespear and running over everyone in his electric wheel chair. There is a clock very low on the wall so your teacher can check the time without looking up.")
Stairs = Room("Stairs", "You are next to the stairs")
Stairs2 = Room("Stairs", "You are next to the stairs on the second floor")
Stairs3 = Room("Stairs", "You are next to the stairs on the third floor")
Cafeteria = Room("Cafeteria", "You are in the cafeteria where many people are sitting before class begins, there appears to be an unattended water bottle on the table. The stairs are to your right and the store is to your left.")
SecondFloor = Room("Second Floor", "You are on the second floor, there isn't much here besides two halls of classes and a lot of windows. Your math class is in the right hall. Your science class is in the left hallway. The stairs and the outside area are in front of you.")
SecondFloorP2 = Room("Between outside area and stairs", "The outside area is in front of you and the stairs are to your right")
Outside2 = Room("Outside area", "You are outside on the second floor, maybe if you try to leave from here no one will notice?")
Math = Room("Math class", "You enter Math class where there are a bunch of cheesy math jokes on the wall and the board is covered in formulas beyond comprehension. There is a clock in here as well but it seems to be covered in math posters.")
Science = Room("Science class", "You enter science with your teacher who looks like modern day Einstein mixing chemicals that are bubbling a little to much. There is another clock in here but it is covered in chemicals which are probably dangerous to touch.")
ThirdFloor = Room("Third Floor", "You enter the third floor where the office and stairs are in front of you, your English class is in the left hallway and the ladder to the roof is in the right hallway")
ThirdFloorP2 = Room("Between office and stairs", "The stairs are to your right and the office is to your left.")
Ladder = Room("Ladder", "There is a ladder that goes to the roof, the only problem is you need a key to access the roof")
Office = Room("Office", "You enter the office where the principle and vice principle are haning out, there is a clock on the wall. You can exchange 4 good student tickets for a battery")
Physical = Room("P.E", "You enter P.E. and you find your teacher pushing the ground down in order to do a push-up.")
Roof = Room("Roof", "You manage to get onto the roof, there is nothing up here besides a vent to your left.")
RoofP2 = Room ("Roof by vent", "You walk over to the other side of the vent and there is a clock on the floor.")
vent = Room("Behind vent", "There is a clock on the floor but it seems to out of batteries")
SecondFloorLH = Room("Left Hallway", "You are in the left hall of the second floor, your science class is in front of you. There seems to be something funny with the plant next to the classroom.")
SecondFloorRH = Room("Right Hallway", "You are in the right hall of the second floor, your second class is back behind you.")
ThirdFloorRH = Room("Right Hallway", "You are in the right hall of the third floor, there is a ladder in front of you and the janitors closet behind you. The bully is here and seems interested in a trade.")
ThirdFloorLH = Room("Left Hallway", "You are in the left hall of the third floor, your fourth class is back behind you.")
Janitor = Room ("Janitor's closet", "You are in the janitor's closet where there are a bunch of cleaning supplies and a towel.")
