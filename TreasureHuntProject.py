print(
    r'''
       _________
      |         |
      | SURVIVE |
      |_________|
          || 
      .-'      `-.
     /            \
    |  WASTELAND   |
     \____________/
        '''
)
print("Welcome to **SURVIVE: The Wasteland**.\nYour mission is to find safety, unravel secrets of the wasteland, and survive its challenges.")

# First Choice
choice1 = input('Your spacecraft crash-landed in a desolate wasteland. Smoke rises from your wrecked ship. \nDo you search for "shelter" or investigate the "wreckage" for clues?\n')
if choice1.lower() == 'shelter':
    print(
        r'''
       __||__
      //    \\
     ||      ||
     ||______||
      \______/
       '''
    )
    print("You walk towards a rocky ridge in search of shelter and find a cave hidden behind thorny bushes.")
    action1 = input('The cave is dark, but there’s faint light deeper inside. Do you "enter" cautiously or "search" around the entrance?\n')
    if action1.lower() == 'enter':
        print("You carefully step inside. The air feels cooler, and you hear dripping water.")
        print("Deeper inside, you stumble upon strange carvings glowing faintly on the walls.")
        action2 = input('Do you "inspect" the carvings or "take water" from the underground stream?\n')
        if action2.lower() == 'inspect':
            print("The carvings depict the fall of an ancient civilization. You touch them, and the walls tremble!")
            print("Behind the wall, you discover an ancient device, humming softly. It looks like a beacon.")
            action3 = input('Do you "activate" the beacon or "leave" it alone?\n')
            if action3.lower() == 'activate':
                print("The beacon lights up, and a map projects into the air. It shows a path to a safe zone!")
                print("You follow the map and set off on your journey, determined to survive.")
            elif action3.lower() == 'leave':
                print("You leave the device untouched and take water before exiting the cave.")
                print("The wasteland feels even more daunting as you venture further without guidance.")
            else:
                print("Invalid choice. The cave collapses, trapping you inside. Game over.")
        elif action2.lower() == 'take water':
            print("You gather fresh water and leave the cave.")
            print("The wasteland stretches endlessly before you, but you feel a bit stronger.")
        else:
            print("Invalid choice. The glowing carvings dim, and the cave collapses. Game over.")
    elif action1.lower() == 'search':
        print("You find strange claw marks around the cave entrance.")
        print("A sudden growl makes you turn around—it’s a predator! You barely escape, but you’re forced to move without shelter.")
    else:
        print("Invalid choice. Night falls, and the freezing temperatures overcome you. Game over.")

elif choice1.lower() == 'wreckage':
    print(
        r'''
      _______
     /       \
    |  SHIP   |
     \_______/
        '''
    )
    print("You return to your wrecked ship. The hull is scorched, but the cargo bay might hold supplies.")
    action1 = input('Do you "enter" the wreckage or "scan" the surroundings for threats?\n')
    if action1.lower() == 'enter':
        print("Inside, you find a survival kit with food, a flare gun, and a strange metallic cube.")
        action2 = input('Do you "take everything" or "leave" the cube?\n')
        if action2.lower() == 'take everything':
            print("The cube hums in your hand. It feels warm and seems to pulse with energy.")
            print("Suddenly, a holographic map projects from the cube, showing a hidden refuge far to the north.")
            print("You take the supplies and follow the map’s path.")
        elif action2.lower() == 'leave':
            print("You take only the essentials and leave the cube behind.")
            print("The journey ahead feels daunting, but you press on, relying on your instincts.")
        else:
            print("Invalid choice. The ship collapses, burying you in the wreckage. Game over.")
    elif action1.lower() == 'scan':
        print("You spot a group of scavengers approaching. They look hostile!")
        action2 = input('Do you "hide" in the wreckage or "run" towards a nearby ridge?\n')
        if action2.lower() == 'hide':
            print("The scavengers loot the wreckage but don’t find you. Once they leave, you quietly gather supplies and continue your journey.")
        elif action2.lower() == 'run':
            print("You sprint towards the ridge, but the scavengers see you and give chase.")
            print("You barely escape, but you’ve lost precious time and energy.")
        else:
            print("Invalid choice. The scavengers catch you. Game over.")
    else:
        print("Invalid choice. The wreckage burns further, destroying all possible resources. Game over.")

# Next Phase (Common Path After Initial Choices)
print(
    r'''
        /\
       //\\
      //  \\
     ||    ||
     ||____||
      \____/
       '''
)
print("After hours of navigating the wasteland, you arrive at a towering metal structure hidden in the dunes.")
print("The structure looks ancient but operational. You notice two entry points: a guarded gate and a service hatch.")
final_choice = input('Do you approach the "gate" or sneak through the "hatch"?\n')
if final_choice.lower() == 'gate':
    print("The guards point their weapons at you, but you raise your hands and show the map/device.")
    print("After a tense moment, they let you in and escort you to their leader.")
    print("Congratulations! You’ve gained the trust of the wasteland survivors and found safety!")
    print(
        r'''
          _______
         /       \
        /  SAFE   \
       |  REFUGE   |
        \_________/
        '''
    )
elif final_choice.lower() == 'hatch':
    print("You crawl through the service hatch and find yourself in a storage room filled with supplies.")
    print("Alarms start blaring! Guards rush in, but you convince them of your peaceful intentions.")
    print("After some negotiation, they accept you into their community.")
    print("You survived and earned a place among the wasteland survivors!")
else:
    print("Invalid choice. The wasteland’s dangers finally overwhelm you. Game over.")
