import csv
import random
import copy
import json


class Armor:
    def __init__(self, name, typeof, movement, protection):
        self.name = name
        self.typeof = typeof
        self.movement = movement
        self.protection = protection

    def __str__(self):
        return f"{self.name} Type: {self.typeof} Movement: {self.movement} Protection: {self.protection}"


def generate(adjectives, names, how_many):
    readArmors = []
    generatedArmors = []

    #Load weapon templates
    with open('GearSource/Armors.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  #strips header row
        for row in reader:
            readArmors.append(Armor("", row[0], row[1], row[2]))
    for x in range(how_many):
        weapon = copy.deepcopy(random.choice(readArmors))
        weapon.name = f"The {random.choice(adjectives).rstrip().title()} Armor of {random.choice(names).rstrip().title()}"
        generatedArmors.append(weapon)

    with open("GearGenerated/GeneratedArmors.json", "w") as f:
        f.write(json.dumps(generatedArmors, default=lambda x: x.__dict__))
