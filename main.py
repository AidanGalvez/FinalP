from Rooms import *
print("\nWelcome to School!\nYou arrive at school for a lockdown to occur due to a virus causing everyone to be stuck at school for a minimum of two months.\nYou have to find a way to escape, your best idea is to take all the clocks so the teachers forget the time. It probably won't work but it's your best and only idea.")
print("\nObjective: Collect all 10 clocks and escape school")
print("Controls: up, down, left, right, forward, back, grab, use, inventory, and controls\n")

movement = ["up","down","left","right","forward","back"]
other = ["grab","use","inventory","controls"]
print(Outside)

class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room
    
    def move(self, direction):
        connections = {
            "Outside": {"forward": "MainArea", "back": "MainArea"},
            "MainArea": {"back": "Outside", "left": "Store", "right": "Gym", "forward": "Stairs"},
            "Store": {"back": "MainArea"},
            "Gym": {"left": "MainArea", "forward": "Physical"},
            "English": {"forward": "ThirdFloorLH"},
            "Stairs": {"up": "SecondFloor"},
            "Stairs2": {"up": "ThirdFloor", "down": "MainArea", "left": "SecondFloorP2"},
            "Stairs3": {"down": "SecondFloor", "left": "ThirdFloorP2"},
            "SecondFloor": {"left": "SecondFloorLH", "right": "SecondFloorRH","forward": "SecondFloorP2"},
            "SecondFloorP2": {"forward": "Outside2", "right": "Stairs2", "back": "SecondFloor"},
            "Outside2": {"back": "SecondFloorP2", "forward" : "SecondFloorP2"},
            "Math": {"forward": "SecondFloorRH"},
            "Science": {"back": "SecondFloorLH"},
            "ThirdFloor": {"left": "ThirdFloorLH", "right": "ThirdFloorRH", "forward": "ThirdFloorP2"},
            "ThirdFloorP2":{"left": "Office", "right": "Stairs3", "back" : "ThirdFloor"},
            "Ladder": {"up": "Roof", "back": "ThirdFloorRH"},
            "Office": {"right": "ThirdFloorP2"},
            "Physical": {"back": "Gym"},
            "Roof": {"down": "ThirdFloorRH"},
            "SecondFloorLH": {"forward": "Science", "right": "SecondFloor"},
            "SecondFloorRH": {"back": "Math", "left": "SecondFloor"},
            "ThirdFloorRH": {"forward": "Ladder", "left": "ThirdFloor"},
            "ThirdFloorLH": {"back": "English", "right": "ThirdFloor"},
        
        }
        
        if direction in connections[self.current_room]:
            self.current_room = connections[self.current_room][direction]
            location = self.current_room
            if location == "MainArea":
                print(MainArea)
            if location == "Outside":
                print(Outside)
            if location == "Store":
                print(Store)
            if location == "Gym":
                print(Gym)
            if location == "English":
                print(English)
            if location == "Stairs" or location == "Stairs2" or location == "Stairs3":
                print(Stairs)
            if location == "SecondFloor":
                print(SecondFloor)
            if location == "SecondFloorP2":
                print(SecondFloorP2)
            if location == "Outside2":
                print(Outside2)
            if location == "Math":
                print(Math)
            if location == "Science":
                print(Science)
            if location == "ThirdFloor":
                print(ThirdFloor)
            if location == "ThirdFloorP2":
                print(ThirdFloorP2)
            if location == "Ladder":
                print(Ladder)
            if location == "Office":
                print(Office)
            if location == "Physical":
                print(Physical)
            if location == "Roof":
                print(Roof)
            if location == "SecondFloorLH":
                print(SecondFloorLH)
            if location == "SecondFloorRH":
                print(SecondFloorRH)
            if location == "ThirdFloorRH":
                print(ThirdFloorRH)
            if location == "ThirdFloorLH":
                print(ThirdFloorLH)

        # if direction not in connections[self.current_room] and direction not in other:
            # print("\nYou cannot go that direction\n")

player = Player("Outside")
while True:
    direction = playerchoice()
    player.move(direction)