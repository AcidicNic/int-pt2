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


# 2. Determine if 2 Strings are anagrams
def are_anagrams(str1, str2):
    return sorted(list(str1.lower())) == sorted(list(str2.lower()))

# 3. Find the shortest palindrome in a String
def shortest_palindrome(text):
    for palindrome_len in reversed(range(3, len(text))):
        for i in range(palindrome_len, len(text)):
            if is_palindrome(text[i-palindrome_len:i]):
                return text[i-palindrome_len:i]
def is_palindrome(text):
    text = text.lower()
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] == text[right]:
            left += 1
            right -= 1
        else:
            return False
    return True
# 4. Write a function that prints out the binary form of an int

# 5. Implement squareroot function


if __name__ == '__main__':
    """ count_islands() test """
    print("\ncount_islands() Tests")
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

    """ are_anagrams() """
    print("\nare_anagrams() Tests")
    # False
    print(are_anagrams("hello", "hell"))
    # True
    print(are_anagrams("cat", "tac"))
    # True
    print(are_anagrams("theeyes", "theysee"))

    """ shortest_palindrome() """
    print("\nshortest_palindrome() Tests")
    # lol
    print(shortest_palindrome("helolo"))
    # None
    print(shortest_palindrome("cat"))
    # teet
    print(shortest_palindrome("teeth"))
    # None
    print(shortest_palindrome("help"))


