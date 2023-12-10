def load(fpath: str):
    with open(fpath) as f:
        return [line.rstrip() for line in f.readlines()]
