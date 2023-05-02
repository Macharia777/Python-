print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')

print("Welcome to Treasure Island. Your mission is to find the treasure.")

light_lighter = input('You are in a room that is dark, you have a note in your hand, there is a barrel with a lighter on top, there is a hole straight ahead, what do you do? "Light lighter", "Choose_hole " ')
#choice2 = "Choose_hole"
#choice3 = ""
if light_lighter != "Light lighter":
    choose_hole = input('will you crawl through the hole? "Yes" or "no" ')
    if choose_hole != "yes":
        print("you have entered a room with two doors, ")
        two_doors = input('What door will you choose? "left" or "right"? ')
        if two_doors == "left":
            print("you are in a beach and in the far distance the there is a ship")
            ship = input('what do you do to see the ship? ')
            if ship == "set fire":
                print("The ship is coming")
                enter_ship = input('The ship looks inhabited by the dead, what do you do? "Enter" or "Not enter? " ')
                if enter_ship == "Enter":
                    print("You are eaten by the zombies")
                else:
                    print("You are eaten by the zombies")
            else:
                print("The ship is gone and you are dead in the god-forsaken island")
        else:
            print("right door")        
    else:
        print("You are stuck")
else:
        print("Exit the door behind you.")
  
#choose_hole = input("what do you do? ")
#hole_note = input("You are now in another room with a note on the floor, what do you do? ")
#escaped_door = input("You see a ship in the distance, craft fire or shout? ")
#board_ship = input("will you board the ship? ")
