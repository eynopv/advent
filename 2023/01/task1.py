from loader import load


def main(task: str):
    values = [getcalibrationvalue(line) for line in task]
    return sum(values)


def getcalibrationvalue(line: str) -> int:
    first = getfirstdigit(line)
    last = getfirstdigit(line[::-1])
    return int(f"{first}{last}")


def getfirstdigit(s: str) -> str:
    for c in s:
        if c.isdigit():
            return c


if __name__ == "__main__":
    task = load("./data/data.txt")
    print(main(task))
