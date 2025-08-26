from GenerateSource import ArmorGenerate, WeaponGenerate, HelmetGenerate
from enum import Enum



if __name__ == '__main__':
    names = open("TextSource/Names.txt", "r").readlines()
    adjectives = open("TextSource/Adjectives.txt", "r").readlines()

    print('Starting to generate weapons...')
    WeaponGenerate.generate(adjectives, names, 1000)
    print('Generated weapons complete!')

    print('Starting to generate armors...')
    ArmorGenerate.generate(adjectives, names, 1000)
    print('Generated armors complete!')

    print('Starting to generate helmets...')
    HelmetGenerate.generate(adjectives, names, 1000)
    print('Generated helmets complete!')
