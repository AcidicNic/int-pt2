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
def int_to_binary(num):
    if not isinstance(num, int):
        return None
    i = -1
    while True:
        if 2 ** (i+1) > num:
            break
        i += 1
    sum = 0
    binary = ""
    for x in reversed(range(i+1)):
        if sum + 2**x > num:
            binary += "0"
        else:
            binary += "1"
            sum += 2**x
    return binary


# 5. Implement squareroot function
def square_root(num):
    if not isinstance(num, int):
        return None
    sqr = 0
    while True:
        if sqr**2 == num:
            return sqr
        elif sqr**2 > num:
            return None
        sqr += 1


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
    print(f'"hello", "hell" -> {are_anagrams("hello", "hell")}')
    # True
    print(f'"cat", "tac" -> {are_anagrams("cat", "tac")}')
    # True
    print(f'"theeyes", "theysee" -> {are_anagrams("theeyes", "theysee")}')

    """ shortest_palindrome() """
    print("\nshortest_palindrome() Tests")
    # lol
    print(f"'helolo' -> {shortest_palindrome('helolo')}")
    # None
    print(f"'cat' -> {shortest_palindrome('cat')}")
    # teet
    print(f"'teeth' -> {shortest_palindrome('teeth')}")
    # None
    print(f"'help' -> {shortest_palindrome('help')}")

    """ int_to_binary() """
    print("\nint_to_binary() Tests")
    print(f"63 -> {int_to_binary(63)}")
    print(f"64 -> {int_to_binary(64)}")
    print(f"65 -> {int_to_binary(65)}")
    print(f"17394 -> {int_to_binary(17394)}")
    print(f"23 -> {int_to_binary(23)}")

    """ square_root() """
    print("\nsquare_root() Tests")
    print(f"1 -> {square_root(1)}")
    print(f"64 -> {square_root(64)}")
    print(f"81 -> {square_root(81)}")
    print(f"55 -> {square_root(55)}")

