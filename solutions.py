# 1. Given a 2D array of 1s and 0s, count the number of "islands of 1s" (e.g. groups of connecting 1s)


def count_islands(island_map):
    w = len(island_map[0])
    h = len(island_map)
    checked_pairs = []
    islands = 0
    for y in range(h):
        if w != len(island_map[y]):
            raise ValueError("Invalid island_map")
        for x in range(w):
            if [y, x] not in checked_pairs:
                if island_map[y][x] == 1:
                    islands += 1
                    checked_pairs.extend(check_nearby(y, x, island_map, checked_pairs))
    return islands


def check_nearby(y, x, island_map, checked_pairs=None):
    # Helper Function for count_islands()
    if not checked_pairs:
        checked_pairs = []
    for yo in range(-1, 2):
        for xo in range(-1, 2):
            if (0 <= x+xo < len(island_map[0])) and (0 <= y+yo < len(island_map)):
                if island_map[y+yo][x+xo] == 1 and (not [y+yo, x+xo] in checked_pairs):
                    checked_pairs.append([y+yo, x+xo])
                    check_nearby(y+yo, x+xo, island_map, checked_pairs)
    return checked_pairs


# 2. Print all permutations of a String

# 3. Find the shortest palindrome in a String

# 4. Write a function that prints out the binary form of an int

# 5. Implement squareroot function

if __name__ == '__main__':
    # Count islands test
    island_map = [
        [1, 0, 0, 1, 0, 0, 1, 1, 0],
        [1, 1, 0, 0, 0, 1, 1, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0]
    ]
    # Should return 4
    print(count_islands(island_map))

    island_map = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    # Should return 0
    print(count_islands(island_map))

    island_map = [
        [1, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 1, 0]
    ]
    # Should return 3
    print(count_islands(island_map))

    island_map = [
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1]
    ]
    # Should return 8
    print(count_islands(island_map))

