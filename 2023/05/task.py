import sys
from typing import Dict, List
from loader import load



def main(data: str) -> None:
    data_dict = parse_data(data)
    seeds = data_dict.get('seeds', [])
    results = [process_seed(seed, data_dict) for seed in seeds]
    smallest = min(results)
    print(f"Smallest: {smallest}")

    seed_ranges = [seeds[i:i+2] for i in range(0, len(seeds), 2)]
    results_range = [process_seed_range(seed_range, data_dict) for seed_range in seed_ranges]
    smallest_range = min(results_range)
    print(f"Smallest range: {smallest_range}")


def process_seed_range(seed_range: List[int], data: Dict[str, List[List[int]]]) -> int:
    print("Trying seed", seed_range)
    maps_order = [
        'seed-to-soil map',
        'soil-to-fertilizer map',
        'fertilizer-to-water map',
        'water-to-light map',
        'light-to-temperature map',
        'temperature-to-humidity map',
        'humidity-to-location map'
    ]

    current_ranges = [seed_range]

    for map_name in maps_order:
        map_data = data.get(map_name, [])
        new_ranges = []
        print(map_name)
        for cr in current_ranges:
            new_ranges += process(cr, map_data)
        current_ranges = new_ranges
        print("CURRENT RANGE", current_ranges)

    print(current_ranges)



def process(seed_range, data):
    # ...S1..S2...E1....E2
    # ...S2..S1...E2....E1
    # ...S2..S1...E1....E2
    # ...S1..S2...E2....E1
    s1 = seed_range[0]
    e1 = s1 + seed_range[1] - 1

    rs = []
    for d in data:
        print(d)
        s2 = d[1]
        e2 = s2 + d[1] - 1
        dst = d[0]

        s = max([s1, s2])
        e = min([e1, e2])
        if e < s:
            continue

        if s1 < s2:
            print('s1 < s2')
            rs += [[dst, s1 - s2 + 1]]
        else:
            rs += [[s1, s1 - s2 + 1]]

        if s1 > s2 and e2 < e1:
            print('s1 > s2 and e1 > s2')
            rs += [[dst, e2 - s2 + 1]]
        
        if e2 < e1:
            print('e2 < e1')
            rs += [[e2, e1 - e2 + 1]]

    print("RS", rs)

    if not rs:
        return [seed_range]
    else:
        return rs


def parse_data(input_data: str) -> Dict[str, List[List[int]]]:
    lines = input_data.strip().split('\n')

    data = {}
    current_key = ''
    current_values = []

    for line in lines:
        if line.startswith('seeds:'):
            seeds_values = line.split(':')[1].strip().split()
            data['seeds'] = list(map(int, seeds_values))
        elif line.endswith(':'):
            if current_key and current_values:
                data[current_key] = current_values
            current_key = line[:-1]
            current_values = []
        else:
            values = line.split()
            if values:  # Check if there are values to convert
                try:
                    int_values = list(map(int, values))
                    current_values.append(int_values)
                except ValueError:
                    pass  # Skip lines that cannot be converted to integers

    if current_key and current_values:
        data[current_key] = current_values

    return data


def process_seed(seed: int, data: Dict[str, List[List[int]]]) -> int:
    current_value = seed

    maps_order = [
        'seed-to-soil map',
        'soil-to-fertilizer map',
        'fertilizer-to-water map',
        'water-to-light map',
        'light-to-temperature map',
        'temperature-to-humidity map',
        'humidity-to-location map'
    ]

    for map_name in maps_order:
        current_map = data.get(map_name, [])
        new_value = -1
        for m in current_map:
            destination, source, rng = m[0], m[1], m[2]
            if source <= current_value <= (source + rng):
                new_value = destination + current_value - source
                break
        current_value = new_value if new_value > 0 else current_value

    return current_value


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Provide data file')
        print('Example: python task.py [data.txt]')
        sys.exit(-1)
    fname = sys.argv[1]
    with open(fname) as f:
        data = f.read()
        main(data)
