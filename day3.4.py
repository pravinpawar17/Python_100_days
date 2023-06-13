#Treasure Island

print('''

*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

''')
print("welcome to the treasure island")
print("your mission is to find the tresure ")
choice1 = input('you are a crossroad, where are you want to go ? Type  "left" or "right". ').lower()
if choice1 == "left":
    choice2 = input('your come to a lake, there is island in middle of lake . Type "waite" to wait for a boat or "swime" to swim across ').lower()
    if choice2 == "waite":
        choice3 = input("you arrive at the island unharmed. there is a house with 3 doors. one is red, one is blue and pne is yello.which colour o you choose?").lower()
        if choice3 == "red":
            print("it's a room full of fire.Game Over")
        elif choice3 == "yellow":
            print("you found the trasure ! you win !!")
        elif choice3 == "blue":
            print("you enter a room of beats. Game over .")
        else:
            print("you choose a door that doesn't exit, Game Over ")
    else:
        print("you got attacked by an angry trout, Game Over ")
else:
    print("you fell into a hole , Game Over")


