import csv
import random
import copy
import json
from GenerateSource.Enums import Rarity


class Helmet:
    def __init__(self, name, typeof, movement, protection, rarity):
        self.name = name
        self.typeof = typeof
        self.movement = movement
        self.protection = protection
        self.rarity = rarity


def generate(adjectives, names, how_many):
    readHelmets = []
    generatedHelmets = []
    #Load weapon templates
    with open('GearTemplates/Helmets.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  #strips header row
        for row in reader:
            rarity = random.choice(list(Rarity))
            readHelmets.append(
                Helmet(
                    "",
                    row[0],
                    float(row[1])*float(rarity.value),
                    float(row[2])*float(rarity.value),
                    rarity.name
                )
            )
    for x in range(how_many):
        helmet = copy.deepcopy(random.choice(readHelmets))
        helmet.name = f"The {random.choice(adjectives).rstrip().title()} Helmet of {random.choice(names).rstrip().title()}"
        generatedHelmets.append(helmet)

    with open("GeneratedWeapons/Helmets.json", "w") as f:
        f.write(json.dumps(generatedHelmets, default=lambda x: x.__dict__))
