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
            "MainArea": {"back": "Outside", "left": "Store", "right": "Gym"},
            "Store": {"back": "MainArea"},
            "Gym": {"left": "MainArea"}
        
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
        if direction not in connections[self.current_room] and direction not in other:
            print("\nYou cannot go that direction\n")

player = Player("Outside")
while True:
    direction = playerchoice()
    player.move(direction)