import csv
import random
import copy
import json
from GenerateSource.Enums import Rarity


class Armor:
    def __init__(self, name, typeof, movement, protection, rarity):
        self.name = name
        self.typeof = typeof
        self.movement = movement
        self.protection = protection
        self.rarity = rarity


def generate(adjectives, names, how_many):
    readArmors = []
    generatedArmors = []

    #Load weapon templates
    with open('GearTemplates/Armors.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  #strips header row
        for row in reader:
            rarity = random.choice(list(Rarity))
            readArmors.append(
                Armor(
                    "",
                    row[0],
                    float(row[1]) * float(rarity.value),
                    float(row[2]) * float(rarity.value),
                    rarity.name
                )
            )
    for x in range(how_many):
        weapon = copy.deepcopy(random.choice(readArmors))
        weapon.name = f"The {random.choice(adjectives).rstrip().title()} Armor of {random.choice(names).rstrip().title()}"
        generatedArmors.append(weapon)

    with open("GearGenerated/Armors.json", "w") as f:
        f.write(json.dumps(generatedArmors, default=lambda x: x.__dict__))
