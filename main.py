from Combat import *
import os
import time


os.system("cls||clear")
print(C.OKBLUE + "Welcome to CombatRPG!" + C.ENDC + "\n")
gameIndex = int(input(C.HEADER + "1 - New Game / 2 - Load Game / 3 - Exit / 4 - Sprints" + C.ENDC + "\n"))
c = Combat()

if gameIndex == 1:
    c.AddPlayer(Player("Patryk", 10, 100, 0, Item("Knife", 30, 15, 30)))
    c.AddPlayer(Player("Bartek", 10, 100, 0, Item("Stick", 30, 15, 30)))
    c.AddOpponent(Player("Maciek", 10, 100, 0, Item("Barbell", 30, 15, 30)))
    c.AddOpponent(Player("Mateusz", 10, 100, 0, Item("Fists", 30, 15, 30)))
    c.Fight()

elif gameIndex == 2:
    os.system("cls||clear")
    print(C.HEADER + "Loading..." + C.ENDC)
    time.sleep(3)
    c.LoadProgress()
    os.system("cls||clear")
    print(C.OKBLUE + "Game has been loaded!" + C.ENDC + "\n\n")
    time.sleep(1)
    print(C.OKCYAN + "Have fun!" + C.ENDC + "\n\n")
    c.Fight()

elif gameIndex == 3:
    os.system("cls||clear")
    print(C.WARNING + "Exiting..." + C.ENDC)
    time.sleep(3)
    os.system("cls||clear")
    print(C.OKCYAN + "Thanks for being a part of our game!" + C.ENDC)

elif gameIndex == 4:
    os.system("cls||clear")
    print(C.WARNING + "Loading Sprints..." + C.ENDC + "\n")
    time.sleep(3)
    os.system("cls||clear")
    print(C.HEADER + "Sprint 1: 23:42 , 20.05.2023" + C.ENDC + "\n\n")
    print(C.BOLD + "SaveProgress function saves some weird things inside players.txt, needs to be fixed," + C.ENDC + "\n")
    print(C.BOLD + "I don't know if LoadProgress function works, will know after SaveProgress starts to work," + C.ENDC + "\n")
    print(C.BOLD + "also I'm not sure why players.txt is saved outside the CombatRPG folder, needs to be fixed." + C.ENDC + "\n")
    time.sleep(10)
    os.system("cls||clear")
    print(C.HEADER + "Sprint 2: 12:21 , 21.05.2023" + C.ENDC + "\n\n")
    print(C.BOLD + "Saving to a file works now," + C.ENDC + "\n")
    print(C.BOLD + "players.txt is now saved inside the CombatRPG folder," + C.ENDC + "\n")
    print(C.BOLD + "I don't know why LoadProgress function still doesn't work, it should work now!" + C.ENDC + "\n")
    time.sleep(6)
    os.system("cls||clear")
    print(C.HEADER + "Sprint 3: 18:56 , 23.05.2023" + C.ENDC + "\n\n")
    print(C.BOLD + "Added the load_attributes function that makes LoadProgress function work," + C.ENDC + "\n")
    print(C.BOLD + "Changed save_attributes function so it is compatibile with the new load_attributes function," + C.ENDC + "\n")
    print(C.BOLD + "LoadProgress now works, also added some small improvements to the UX." + C.ENDC + "\n")
    time.sleep(10)

else:
    os.system("cls||clear")
    print(C.FAIL + "ERROR" + C.ENDC + "\n")
    time.sleep(1)
    os.system("cls||clear")
    print(C.WARNING + "YOUR COMPUTER WILL EXPLODE IN: " + C.ENDC + "\n")
    time.sleep(1)
    print(C.BOLD + "3" + C.ENDC + "\n")
    time.sleep(1)
    print(C.BOLD + "2" + C.ENDC + "\n")
    time.sleep(1)
    print(C.BOLD + "1" + C.ENDC + "\n")
    time.sleep(1)
    os.system("cls||clear")
    print(C.OKGREEN + "Just kidding :)" + C.ENDC)