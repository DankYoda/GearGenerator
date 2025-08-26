import csv
import random
import copy
import json


class Helmet:
    def __init__(self, name, typeof, movement, protection):
        self.name = name
        self.typeof = typeof
        self.movement = movement
        self.protection = protection

    def __str__(self):
        return f"{self.name} Type: {self.typeof} Movement: {self.movement} Protection: {self.protection}"


def generate(adjectives, names, how_many):
    readHelmets = []
    generatedHelmets = []

    #Load weapon templates
    with open('GearSource/Helmets.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  #strips header row
        for row in reader:
            readHelmets.append(Helmet("", row[0], row[1], row[2]))
    for x in range(how_many):
        weapon = copy.deepcopy(random.choice(readHelmets))
        weapon.name = f"The {random.choice(adjectives).rstrip().title()} Helmet of {random.choice(names).rstrip().title()}"
        generatedHelmets.append(weapon)

    with open("GearGenerated/GeneratedHelmets.json", "w") as f:
        f.write(json.dumps(generatedHelmets, default=lambda x: x.__dict__))
