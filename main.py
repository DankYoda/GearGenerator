import GenerateSource.WeaponGenerate as WeaponGenerate


class Helmet:
    def __init__(self, name, typeof, movement, protection):
        self.name = name
        self.typeof = typeof
        self.movement = movement
        self.protection = protection


class Armor:
    def __init__(self, name, typeof, movement, protection):
        self.name = name
        self.typeof = typeof
        self.movement = movement
        self.protection = protection


if __name__ == '__main__':
    names = open("GearSource/Names.txt", "r").readlines()
    adjectives = open("GearSource/Adjectives.txt", "r").readlines()

    print('Starting to generate weapons...')
    WeaponGenerate.generate(adjectives, names, 100)
    print('Generated weapons complete!')
