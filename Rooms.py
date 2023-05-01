class Room:
    def __init__(self, name, description, maps = "", items = [], direction = ""):
        self.__name = name
        self.__description = description
        self.__items = items
        self.__maps = maps
        self.__direction = direction
    
    def __str__(self):
        return f" \n\n{self.__maps}\n\nLocation: {self.__name}, {self.__description}\n"

def playerchoice():
    inventory = Inventory()
    choice = input("What would you like to do?\n").lower()
    while choice not in ["up", "down", "left", "right", "forward", "back", "grab", "use", "inventory", "controls"]:
        print(f'"{choice}" is not a valid option\n')
        choice = input("What would you like to do?\n").lower()
    if choice == "inventory":
        inventory.show_inventory()
    return choice

class Inventory:
    def __init__(self):
        self.__items = []
    
    def add_item(self, item):
        self.__items.append(item)
    
    def remove_item(self, item):
        if item in self.items:
            self.__items.remove(item)
    
    def show_inventory(self):
        if len(self.__items) == 0:
            print("\nYour inventory is empty.\n")
        else:
            print("\nYour inventory contains:")
            for item in self.__items:
                print("- " + item)

        

# rooms
Outside = Room("Outside", "You are outside of school looking up at the building regretting showing up, you can go into the school or try to leave.", " | Main Area |\n |___________|\n |  OutSide  |\n |     X     |\n |___________|")
MainArea = Room("MainArea", "You are in the main area, there are lunch tables with people working on their homework before class. You see a store in the corner of the room that sells various items that may help you get through the day. You also see stairs in front of you that lead upstairs. To the very right of the main area you can see the gym.","\n _____________                                  ___________\n|             |                                 |         |\n|    Store    |                                 |   P.E.  |\n|             |                                 |         |\n|_____   _____|                                 |___   ___|__________\n|             |______|/ \|________              |                    |\n|                        Stairs  |              |                    |\n|                                |______________|         Gym        |\n|                X                                                   |\n|           Main Area                                                |\n|____________________________________________________________________|")
Store = Room("Store", "There is mostly junk in here but they do have gummies I can buy. You see a clock on the wall out of the corner of your eye.", " _____________\n|             |\n|    Store    |\n|      X      |\n|_____   _____|")
Gym = Room("Gym", "You enter the gym which is full of equipment and there is someone doing calf raises in the corner, they look thirsty. You also see your first period class P.E. in front of you. You can also return to the main area.", "      ___________\n      |         |\n      |   P.E.  |\n      |         |\n      |___   ___|__________\n      |                   |\n      |                   |\n______|        Gym        |\n                X         |\n                          |\n                          |\n__________________________|")
English = Room("English class", "You enter your English class where the teacher is reciting Shakespear and running over everyone in his electric wheel chair. There is a clock very low on the wall so your teacher can check the time without looking up.", "__| |_____\n|         |\n| English |\n|    X    |\n|_________|")
Stairs = Room("Stairs", "You are next to the stairs", "__|/ \|__")
SecondFloor = Room("Second Floor", "You are on the second floor, there isn't much here besides two halls of classes and a lot of windows. Your second class is in the right hall. Your third class is in the left hallway. The stairs and the outside area are in front of you.", "                  ______________\n                  |   Outside  |\n                  |            |\n __________       |____|  |____|______\n |        |       |            |      |\n |Science |       |            |_/  \_|______ \n |_      _|       |                   Stairs|\n___|_  _|_________|                         |__________________\n|                        X                                    |\n|                    SecondFloor                              |\n|_______________________________________________________ _____|\n                                               _______|   |___ \n                                               |             |    \n                                               |     Math    |    \n                                               |_____________|")
SecondFloorP2 = Room("Between Outside area and stairs", "The outside area is in front of you and the stairs are to your right","                  ______________\n                  |   Outside  |\n                  |            |\n                  |____|  |____|______\n                  |            |      |\n                  |            |_/  \_|______ \n                  |        X          Stairs|\n                  |                         |")
Outside2 = Room("Outside area", "You are outside on the second floor, maybe if you try to leave from here no one will notice?", "_____________\n|  Outside  |\n|     X     |\n|___|  |____|")
Math = Room("Math class", "You enter Math class where there are a bunch of cheesy math jokes on the wall and the board is covered in formulas beyond comprehension. There is a clock in here as well but it seems to be covered in math posters.", "_______|   |___\n|      X      |\n|     Math    |\n|_____________|")
Science = Room("Science class", "You enter science with a teacher that looks like modern day Einstein mixing chemicals that are bubbling a little to much. There is another clock in here but it is covered in chemicals that might be dangerous to touch.", "__________\n|    X   |\n|Science |\n|_      _|\n _|_  _|_") # if use grab (you should get something to clean the clock off)
ThirdFloor = Room("Third Floor", "You enter the third floor where the office is in front of you, there are also two halls to either side of you.","       __________________________________\n       |           |             |      |\n       |   Office                |_/  \_|_____\n       |           |                  Stairs |\n_______|___________|                         |________|/\|_____\n|                             X                        Ladder |\n|                        Third Floor                          |\n|_____ _______________________________________________________|\n   __| |______\n   |         |\n   | English |\n   |         |\n   |_________|")
ThirdFloorP2 = Room("Between office and stairs", "The stairs are to your right and the office is to your left.", "       __________________________________\n       |           |             |      |\n       |   Office                |_/  \_|_____\n       |           |      X           Stairs |\n_______|___________|                         |")
Ladder = Room("Ladder", "There is a ladder that goes to the roof, the only problem is you need a key to access the roof","|________|/\|_____\n             Ladder")
Office = Room("Office", "You enter the office where the principle and vice principle are haning out.", "       _____________\n       |           |             \n       |   Office                \n       |     X     |\n       |___________|")
Physical = Room("P.E", "You enter P.E. and you find your teacher pushing the ground down in order to do a push-up.", "___________\n|         |\n|   P.E.  |\n|    X    |\n|___   ___|")
Roof = Room("Roof", "You manage to get onto the roof, there is nothing up here besides a vent.", "       __________________________________\n       |                                |\n       |                                |____________________\n       |                                                    |  \n_______|  _____                                             |__\n|         |   |                                               |\n|         |   |            Roof                               |\n|        o|___|              X                                |\n|                                              /\ Ladder      |\n|                                                             |\n|                                                             |\n|_____________________________________________________________|\n")
SecondFloorLH = Room("Left Hallway", "You are in the left hall of the second floor, your third class is to your right.", "                  ______________\n                  |   Outside  |\n                  |            |\n __________       |____|  |____|______\n |        |       |            |      |\n |Science |       |            |_/  \_|______ \n |_      _|       |                   Stairs|\n___|_  _|_________|                         |__________________\n|                                                             |\n|    X               SecondFloor                              |\n|_______________________________________________________ _____|\n                                               _______|   |___ \n                                               |             |    \n                                               |     Math    |    \n                                               |_____________|")
SecondFloorRH = Room("Right Hallway", "You are in the right hall of the second floor, your second class is to your right.", "                  ______________\n                  |   Outside  |\n                  |            |\n __________       |____|  |____|______\n |        |       |            |      |\n |Science |       |            |_/  \_|______ \n |_      _|       |                   Stairs|\n___|_  _|_________|                         |__________________\n|                                                             |\n|                    SecondFloor                        X     |\n|_______________________________________________________ _____|\n                                               _______|   |___ \n                                               |             |    \n                                               |     Math    |    \n                                               |_____________|")
ThirdFloorRH = Room("Right Hallway", "You are in the right hall of the third floor, there is a ladder to your left.", "       __________________________________\n       |           |             |      |\n       |   Office                |_/  \_|_____\n       |           |                  Stairs |\n_______|___________|                         |________|/\|_____\n|                                                      Ladder |\n|                        Third Floor                      X   |\n|_____ _______________________________________________________|\n   __| |______\n   |         |\n   | English |\n   |         |\n   |_________|")
ThirdFloorLH = Room("Left Hallway", "You are in the left hall of the third floor, your fourth class is to your left.", "       __________________________________\n       |           |             |      |\n       |   Office                |_/  \_|_____\n       |           |                  Stairs |\n_______|___________|                         |________|/\|_____\n|                                                      Ladder |\n|     X                  Third Floor                          |\n|_____ _______________________________________________________|\n   __| |______\n   |         |\n   | English |\n   |         |\n   |_________|")
