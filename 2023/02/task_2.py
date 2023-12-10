from loader import load


def main(data):
    sets = [getminimumset(game) for game in data]
    powers = [calculatepower(cubes) for cubes in sets]
    print(sum(powers))


def getminimumset(game):
    gameid, turns = game.split(": ")
    turns = turns.split("; ")
    highest = {"red": 0, "green": 0, "blue": 0}
    for turn in turns:
        cubes = turn.split(", ")
        for cube in cubes:
            num, color = cube.split()
            if highest[color] < int(num):
                highest[color] = int(num)
    return highest


def calculatepower(cubes):
    power = 1
    for num in cubes.values():
        power *= num
    return power


if __name__ == "__main__":
    data = load("./data.txt")
    main(data)
