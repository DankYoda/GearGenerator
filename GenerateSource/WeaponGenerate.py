import csv
import random
import copy
import json
from GenerateSource.Enums import Rarity

class Weapon:
    def __init__(self, name, typeof, hands, attack_range, attack_speed, rarity):
        self.name = name
        self.typeof = typeof
        self.hands = hands
        self.attack_range = attack_range
        self.attack_speed = attack_speed
        self.rarity = rarity


def generate(adjectives, names, how_many):
    readWeapons = []
    generatedWeapons = []

    #Load weapon templates
    with open('GearTemplates/Weapons.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  #strips header row
        for row in reader:
            rarity = random.choice(list(Rarity))
            readWeapons.append(
                Weapon(
                    "",
                    row[0],
                    row[1],
                    float(row[2]) * float(rarity.value),
                    float(row[3]) * float(rarity.value),
                    rarity.name
                )
            )
    for x in range(how_many):
        weapon = copy.deepcopy(random.choice(readWeapons))
        weapon.name = f"The {random.choice(adjectives).rstrip().title()} {weapon.typeof.rstrip().title()} of {random.choice(names).rstrip().title()}"
        generatedWeapons.append(weapon)

    with open("GearGenerated/Weapons.json", "w") as f:
        f.write(json.dumps(generatedWeapons, default=lambda x: x.__dict__))
