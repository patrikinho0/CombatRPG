from Colors import bcolors as C
from Player import Player
from Item import *
import os
import time

class Combat:
    def __init__(self) -> None:
        self.team1 = []
        self.team2 = []

    def SaveProgress(self):
        with open("players.txt", "w") as file:
            file.write("Team1:\n")
            for player in self.team1:
                player.save_attributes(file)
            file.write("\nTeam2:\n")
            for player in self.team2:
                player.save_attributes(file)

    def LoadProgress(self):
        with open("players.txt", "r") as file:
            lines = file.readlines()
            
        team1_started = False
        team2_started = False

        for line in lines:
            line = line.strip()
            if line == "Team1:":
                team1_started = True
                continue
            elif line == "Team2:":
                team1_started = False
                team2_started = True
                continue
            if team1_started or team2_started:
                player = Player.load_attributes(line)
                if player is not None:
                    if team1_started:
                        self.team1.append(player)
                    elif team2_started:
                        self.team2.append(player)

    def AddPlayer(self, player):
        self.team1.append(player)
    
    def ShowTeam(self, team):
        i = 0
        if team == 1:
            for player in self.team1:
                print(i,": ",end="")
                player.ShowStats()
                i+=1
        else:
            for player in self.team2:
                print(i,": ",end="")
                player.ShowStats()
                i+=1

    def AddOpponent(self, player):
        self.team2.append(player)

    def Fight(self):
        while True:
            os.system("cls||clear")
            self.ShowTeam(1)
            print(C.OKGREEN + "-------------------------------" + C.ENDC)
            self.ShowTeam(2)
            playerIndex = int(input(C.OKCYAN + "Pick Player: " + C.ENDC))
            os.system("cls||clear")
            self.team1[playerIndex].ShowStats()
            print(C.OKGREEN + "-------------------------------" + C.ENDC)
            self.ShowTeam(2)
            opponentIndex = int(input(C.OKCYAN + "Pick Opponent: " + C.ENDC))
            os.system("cls||clear")
            self.team1[playerIndex].ShowStats()
            print(C.OKGREEN + "-------------------------------" + C.ENDC)
            self.team2[opponentIndex].ShowStats()
            print(C.FAIL + "Players fighting..." + C.ENDC)
            time.sleep(3)
            playerDMG = self.team1[playerIndex].Attack()
            opponentDMG = self.team2[opponentIndex].dmg
            self.team2[opponentIndex].ModifyHP(playerDMG)
            print(C.BOLD + "Player deals: ", playerDMG, "damage to opponent" + C.ENDC)
            time.sleep(1)
            if self.team2[opponentIndex].HP > 0:
                self.team1[playerIndex].ModifyHP(opponentDMG)
                print(C.BOLD + "Opponent deals: ", opponentDMG, "damage to player" + C.ENDC)
            else:
                print(C.OKGREEN + "Opponent is dead" + C.ENDC + "\n\n")
                self.team2.pop(opponentIndex)
                self.team1[playerIndex].LevelUp()
            
            option = int(input(C.HEADER + "Continue - 1 / Save - 2 / Exit - 3" + C.ENDC + "\n"))

            if option == 1:
                continue

            elif option == 2:
                self.SaveProgress()
                os.system("cls||clear")
                print(C.OKGREEN + "Saving..." + C.ENDC)
                time.sleep(3)
                os.system("cls||clear")
                print(C.OKGREEN + "Your game has been saved! Thanks for playing!" + C.ENDC)
                return
            
            elif option == 3:
                os.system("cls||clear")
                print(C.FAIL + "Exiting..." + C.ENDC)
                time.sleep(3)
                os.system("cls||clear")
                print(C.WARNING + "Game exited without saving! Thanks for playing!" + C.ENDC)
                return
            
            else:
                print(C.FAIL + "ERROR" + C.ENDC)
                return