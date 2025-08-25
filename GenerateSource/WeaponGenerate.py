import csv
import random
import copy
import json


class Weapon:
    def __init__(self, name, typeof, hands, attack_range, attack_speed, ):
        self.name = name
        self.typeof = typeof
        self.hands = hands
        self.attack_range = attack_range
        self.attack_speed = attack_speed

    def __str__(self):
        return f"{self.name} Type: {self.typeof} Hands: {self.hands} Attack Range: {self.attack_range} Attack Speed: {self.attack_speed}"


def generate(adjectives, names, how_many):
    readWeapons = []
    generatedWeapons = []

    #Load weapon templates
    with open('GearSource/Weapons.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  #strips header row
        for row in reader:
            readWeapons.append(Weapon("", row[0], row[1], row[2], row[3]))
    for x in range(how_many):
        weapon = copy.deepcopy(random.choice(readWeapons))
        weapon.name = f"The {random.choice(adjectives).rstrip().title()} {weapon.typeof.rstrip().title()} of {random.choice(names).rstrip().title()}"
        generatedWeapons.append(weapon)

    with open("GearGenerated/GeneratedWeapons.json", "w") as f:
        f.write(json.dumps(generatedWeapons, default=lambda x: x.__dict__))
