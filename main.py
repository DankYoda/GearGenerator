from GenerateSource import ArmorGenerate, WeaponGenerate, HelmetGenerate

if __name__ == '__main__':
    names = open("GearSource/Names.txt", "r").readlines()
    adjectives = open("GearSource/Adjectives.txt", "r").readlines()

    print('Starting to generate weapons...')
    WeaponGenerate.generate(adjectives, names, 100)
    print('Generated weapons complete!')

    print('Starting to generate armors...')
    ArmorGenerate.generate(adjectives, names, 100)
    print('Generated armors complete!')

    print('Starting to generate helmets...')
    HelmetGenerate.generate(adjectives, names, 100)
    print('Generated helmets complete!')
