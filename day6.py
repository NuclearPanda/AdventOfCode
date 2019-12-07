test = "COM)B,B)C,C)D,D)E,E)F,B)G,G)H,D)I,E)J,J)K,K)L".split(',')

global_planets = []


class Planet:

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

    def find_orbits(self, destination=None):
        total = 0
        parent = self.parent
        while not (parent is None or parent == destination):
            total += 1
            parent = parent.parent
        return total

    def find_parents(self):
        parents = []
        parent = self.parent
        while parent is not None:
            parents.append(parent)
            parent = parent.parent
        return parents

    def __str__(self):
        return self.name


def find_planet(name: str, planets: list) -> Planet:
    for item in planets:
        if item.name == name:
            return item


def find_shared_parent(planet1, planet2):
    parents1 = planet1.find_parents()
    parents2 = planet2.find_parents()
    for item in parents1:
        if item in parents2:
            return item


with open("day6input.txt") as f:
    for line in f:
        line = line.strip()
        line = line.split(')')
        planet0 = find_planet(line[0], global_planets)
        planet1 = find_planet(line[1], global_planets)
        if planet0 is None:
            planet0 = Planet(line[0])
            global_planets.append(planet0)
        if planet1 is None:
            planet1 = Planet(line[1])
            global_planets.append(planet1)
        planet1.parent = planet0

total = 0
for planet in global_planets:
    #print(planet, planet.find_orbits())
    total += planet.find_orbits()

print(total)

you = find_planet("YOU", global_planets)
san = find_planet("SAN", global_planets)
shared_parent = find_shared_parent(you, san)
print(you.find_orbits(shared_parent) + san.find_orbits(shared_parent))