from loader import load


COLOR_MAX = {"red": 12, "green": 13, "blue": 14}


def main(data):
    possible = [game for game in data if isgamepossible(game)]
    value = sum([int(game.split(": ")[0].split()[1]) for game in possible])
    print(f"SUM: {value}")


def isgamepossible(game):
    gameid, turns = game.split(": ")
    turns = turns.split("; ")
    for turn in turns:
        if not isturnpossible(turn):
            return False
    return True


def isturnpossible(turn):
    cubes = turn.split(", ")
    for cube in cubes:
        num, color = cube.split(" ")
        if int(num) > COLOR_MAX[color]:
            return False
    return True


if __name__ == "__main__":
    example_1 = "./example_1.txt"
    data = load("./data.txt")
    main(data)
