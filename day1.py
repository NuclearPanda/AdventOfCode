def fuel(mass: int):
    return mass // 3 - 2


def theRocketEq(mass: int):
    neededFuel = fuel(mass)
    totalFuel = neededFuel
    while neededFuel > 0:
        neededFuel = fuel(neededFuel)
        if neededFuel < 0:
            break
        totalFuel += neededFuel
    return totalFuel


print(theRocketEq(100756))
sum = 0
with open("day1Input.txt") as f:
    for i in range(100):
        sum += theRocketEq(int(f.readline()))

print(sum)
