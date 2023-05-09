from Rooms import *
print("\nWelcome to School!\nYou arrive at school for a lockdown to occur due to a virus causing everyone to be stuck at school for a minimum of two months.\nYou have to find a way to escape, your best idea is to take all the clocks so the teachers forget the time. It probably won't work but it's your best and only idea.")
print("\nObjective: Collect all 10 clocks and escape school")
print("Controls: up, down, left, right, forward, back, grab, use, inventory, and controls\ncontrol shows the current amount of clocks you have")
clockcount = []
clock_message_printed = False
print(Outside)
player = Player("Outside", clockcount)
while True:
    direction = player.playerchoice()
    player.move(direction)
    if len(player.clockcount) == 10:
        if not clock_message_printed:
            print("\n\nYou have collected all the clocks you need to escape! Head to the front of the school and leave!\n\n")
            clock_message_printed = True

        if player.current_room == "Outside":
            done = input("\nYou have escaped! Would you like to quit? (quit)\n").lower()
            if done == "quit":
                break

            