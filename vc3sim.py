import random

small_biped = {
    'metal_plate' : [0, 1, 2, 3],
    'severed_cable' : [4, 5, 6, 7],
    'speedup' : [8, 9, 10],
    'speedup_1' : [11, 12],
    'speedup_2' : [13]
}

stubby = {
    'rusted_clump' : [0, 1, 2, 3, 4, 5, 6, 7],
    'broken_key' : [8, 9, 10, 11, 12, 13, 14, 15],
    'small_gear' : [16, 17],
    'evu' : [18, 19, 20],
    'evu_1' : [21, 22],
    'evu_2' : [23]
}

desert_flyer = {
    'metal_plate' : [0, 1, 2, 3, 4, 5, 6, 7],
    'taunt' : [8, 9, 10, 11, 12, 13],
    'taunt_1' : [14, 15, 16, 17],
    'taunt_2' : [18, 19]
}

amusement_flyer = {
    'metal_plate' : [0, 1, 2, 3, 4, 5, 6, 7],
    'rusty_bolt' : [8, 9, 10, 11, 12, 13, 14, 15],
    'dru' : [16, 17, 18, 19, 20, 21],
    'dru_1' : [22, 23, 24, 25],
    'dru_2' : [26, 27]
}

def vc3droplambda(x):
    if "metal_plate" in x and "severed_cable" in x:
        return x["metal_plate"] >= 4 and x["severed_cable"] >=3
    return False

runData = []

runs = int(input("How many times do you want to run the simulation? "))

for r in range (1, runs+1):
    drops = []
    drops1 = []
    drops2 = []

    print()
    print("Desert Fliers")
    for x in range (1, 4):
        roll = random.randint(0,99)
        print(f"{x}: {roll}")
        for k, v in desert_flyer.items():
            if roll in v:
                print(k)
                drops.append(k)

    print()
    print('Pit')
    for x in range (1, 41):
        roll = random.randint(0,99)
        print(f"{x}: {roll}")
        if (x % 2) == 0:
            for k, v in small_biped.items():
                if roll in v:
                    print(k)
                    drops1.append(k)
        else:
            for k, v in stubby.items():
                if roll in v:
                    print(k)
                    drops1.append(k)

    print()
    print("Amusement Park Flyer")
    roll = random.randint(0,99)
    print(f"1: {roll}")
    for k, v in amusement_flyer.items():
        if roll in v:
            print(k)
            drops2.append(k)

    # Count only last 10 drops from fight.
    drops1 = drops1[-10:]

    # Duplicate drops from each section.
    drops = [val for val in drops for _ in (0, 1)]
    drops1 = [val for val in drops1 for _ in (0, 1)]
    drops2 = [val for val in drops2 for _ in (0, 1)]

    # Append pit and amusement drops to flyer drops.
    drops += drops1 + drops2
    dropsDict = {}
    for drop in drops:
        if drop not in dropsDict:
            dropsDict[drop] = 0
        dropsDict[drop] += 1

    runData.append(dropsDict)

# All runs that get VC3
filteredRunData = list(filter(vc3droplambda, runData))
filteredRunDataWithTaunt = list(filter(lambda t: "taunt" in t or "taunt_1" in t or "taunt_2" in t, filteredRunData))

success = len(filteredRunData)
failure = runs - success

print()
print("Results:")
print()

print(f"Successes: {success}")
print(f"Failures: {failure}")

rate = round((success / runs * 100), 2)
tauntRate = round((len(filteredRunDataWithTaunt) / runs * 100), 2)

print()
print(f"VC3 Success Rate: {rate} %")
print(f"VC3 with Taunt Success Rate: {tauntRate} %")
print()
print(f"Attempts: {runs}")

