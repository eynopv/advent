from loader import load


DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def main(task: str):
    values = [getcalibrationvalue(line) for line in task]
    return sum(values)


def getcalibrationvalue(line: str) -> int:
    alldigits = getalldigits(line)
    return int(f"{alldigits[0]}{alldigits[-1]}")


def getalldigits(s: str) -> str:
    ds = []
    for i in range(len(s)):
        if s[i].isdigit():
            ds.append(s[i])
            continue

        for worddigit in DIGITS:
            if s[i:].startswith(worddigit):
                ds.append(DIGITS[worddigit])
                continue
    return ds


if __name__ == "__main__":
    task = load("./data/data.txt")
    print(main(task))
