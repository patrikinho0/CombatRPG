from Item import *
from Colors import bcolors as C

class Player:
    def __init__(self, name, dmg, HP, exp, item) -> None:
        self.HP = HP
        self.item = item
        self.name = name
        self.exp = exp
        self.dmg = dmg

    def save_attributes(self, file):
        file.write(f"{self.name} {self.dmg} {self.HP} {self.exp} {self.item.name} {self.item.dmg} {self.item.critDMG} {self.item.critChance}\n")

    def load_attributes(line):
        player_data = line.split()
        if not player_data:
            return None
        
        name = player_data[0]
        dmg = int(player_data[1])
        HP = float(player_data[2])
        exp = int(player_data[3])
        item_name = player_data[4]
        item_dmg = float(player_data[5])
        item_critDMG = float(player_data[6])
        item_critChance = float(player_data[7])

        item = Item(item_name, item_dmg, item_critDMG, item_critChance)
        return Player(name, dmg, HP, exp, item)

    def ShowStats(self):
        print(self.name, end=" * ")
        print(C.WARNING + "DMG" + C.ENDC, self.dmg, end=" * ")
        print(C.FAIL + "HP" + C.ENDC, self.HP, end=" * ")
        print(C.HEADER + "XP" + C.ENDC, self.exp, end=" * ")
        self.item.ShowStats()
    
    def Attack(self):
        return self.dmg + self.item.Use() + self.exp
    
    def ModifyHP(self, mod):
        self.HP -= mod

    def LevelUp(self):
        self.exp += 1