def adjecent_same(n: int):
    n = str(n)
    for i in range(len(n) - 1):
        if n[i] == n[i + 1]:
            return True
    return False


def adjecent_same_2(n: int):
    n = str(n)
    last_char = None
    adjecent_count = 1
    for char in n:
        if char == last_char:
            adjecent_count += 1
        else:
            if adjecent_count == 2:
                return True
            adjecent_count = 1
            last_char = char
    if adjecent_count == 2:
        return True
    else:
        return False


def ascending(n: int):
    n = str(n)
    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            return False
    return True


counter = 0

# part 1
for candidate in range(125730, 579381):
    if ascending(candidate) and adjecent_same(candidate):
        counter += 1

print(counter)

counter2 = 0
for candidate in range(125730, 579381):
    if ascending(candidate) and adjecent_same_2(candidate):
        counter2 += 1

print(counter2)
