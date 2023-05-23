import random

class Item:
    def __init__(self, name, dmg, critDMG, critChance) -> None:
        self.name = name
        self.dmg = dmg
        self.critDMG = critDMG
        self.critChance = critChance

    def Use(self):
        fullDmg = self.dmg
        randChance = random.randint(0,100)
        if self.critChance >= randChance:
            fullDmg += self.critDMG
        return fullDmg
    
    def to_dict(self):
        return {
            "name": self.name,
            "dmg": self.dmg,
            "critDMG": self.critDMG,
            "critChance": self.critChance
        }
    
    def from_dict(data):
        name = data["name"]
        dmg = data["dmg"]
        critDMG = data["critDMG"]
        critChance = data["critChance"]
        return Item(name, dmg, critDMG, critChance)
    
    def ShowStats(self):
        print(self.name, self.dmg,"+", self.critDMG,"crit", self.critChance, "%")

