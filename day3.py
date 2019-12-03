visited = dict()

global_x = 0
global_y = 0

with open("day3input.txt") as f:
    steps = f.read()

wires = steps.split("\n")
wire1_steps = wires[0].split(",")
wire2_steps = wires[1].split(",")


def walk_global(n: int, direction: str, wireNr: int):
    global global_x
    global global_y
    global visited
    if direction == "U":
        while n > 0:
            global_y += 1
            n -= 1
            if (global_x, global_y) in visited:
                if visited[(global_x, global_y)] != wireNr:
                    visited[(global_x, global_y)] = "X"
            else:
                visited[(global_x, global_y)] = wireNr

    elif direction == "D":
        while n > 0:
            global_y -= 1
            n -= 1
            if (global_x, global_y) in visited:
                if visited[(global_x, global_y)] != wireNr:
                    visited[(global_x, global_y)] = "X"
            else:
                visited[(global_x, global_y)] = wireNr

    elif direction == "R":
        while n > 0:
            global_x += 1
            n -= 1
            if (global_x, global_y) in visited:
                if visited[(global_x, global_y)] != wireNr:
                    visited[(global_x, global_y)] = "X"
            else:
                visited[(global_x, global_y)] = wireNr

    elif direction == "L":
        while n > 0:
            global_x -= 1
            n -= 1
            if (global_x, global_y) in visited:
                if visited[(global_x, global_y)] != wireNr:
                    visited[(global_x, global_y)] = "X"
            else:
                visited[(global_x, global_y)] = wireNr


def find_all_x(visited):
    out = []
    for key in visited.keys():
        if visited[key] == "X":
            out.append(key)
    return out


def find_closest_x(visited):
    currentMin = float("inf")
    currentBest = tuple()
    for key in visited.keys():
        if visited[key] == "X":
            if abs(key[0]) + abs(key[1]) < currentMin:
                currentBest = key
                currentMin = abs(key[0]) + abs(key[1])
    return currentBest, currentMin


for step in wire1_steps:
    walk_global(int(step[1:]), step[0], 1)

global_x = 0
global_y = 0

for step in wire2_steps:
    walk_global(int(step[1:]), step[0], 2)

print(find_closest_x(visited))


def find_smallest_delay_x(steps1: list, steps2: list, intersections: list):
    min_delay_intersection = None
    min_delay = float("inf")
    for intersection in intersections:
        dist1 = walk_to_goal(steps1, intersection)
        dist2 = walk_to_goal(steps2, intersection)
        if dist1 + dist2 < min_delay:
            min_delay = dist1 + dist2
            min_delay_intersection = intersection
    return min_delay_intersection, min_delay


def walk_to_goal(instructions: list, goal: tuple, x=0, y=0):
    total_steps = 0
    for instruction in instructions:
        n = int(instruction[1:])
        direction = instruction[0]
        if direction == "U":
            while n > 0:
                y += 1
                n -= 1
                total_steps += 1
                if (x, y) == goal:
                    return total_steps
        elif direction == "D":
            while n > 0:
                y -= 1
                n -= 1
                total_steps += 1
                if (x, y) == goal:
                    return total_steps
        elif direction == "R":
            while n > 0:
                x += 1
                n -= 1
                total_steps += 1
                if (x, y) == goal:
                    return total_steps
        elif direction == "L":
            while n > 0:
                x -= 1
                n -= 1
                total_steps += 1
                if (x, y) == goal:
                    return total_steps
    raise RuntimeError("Goal not found, reached end of wire")


print(find_smallest_delay_x(wire1_steps, wire2_steps, find_all_x(visited)))
