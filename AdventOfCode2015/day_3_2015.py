"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an
elf at the North Pole calls him via radio and tells him where to move next. Moves are
always exactly one house to the north (^), south (v), east (>), or west (<). After each
move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his
directions are a little off, and Santa ends up visiting some houses more than once.
How many houses receive at least one present?

For example:

    > delivers presents to 2 houses: one at the starting location, and one to the east.
    ^>v< delivers presents to 4 houses in a square, including twice to the house at his
    starting/ending location.
    ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

"""
with open("AdventOfCode2015/tasks/3.txt") as f:
    bfd = f.read()
    coords = [(0, 0)]  # houses
    santa_list = [0, 0]  # coordinates
    for char in bfd:
        match char:
            case ">":
                santa_list[0] += 1
            case "<":
                santa_list[0] -= 1
            case "^":
                santa_list[1] += 1
            case "v":
                santa_list[1] -= 1
        coords.append((santa_list[0], santa_list[1]))

    visited_at_least = len(set(coords))
    print(f"on the first year Santa visited: {visited_at_least}")

"""
--- Part Two ---

The next year, to speed up the process, Santa creates a robot version of himself,
Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same
starting house), then take turns moving based on instructions from the elf, who is
eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

    ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa
    goes south.
    ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where
    they started.
    ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and
    Robo-Santa going the other.


"""
santa_list = [0, 0]
r_santa_list = [0, 0]
coords = [(0, 0)]
i = 0
for char in bfd:
    i += 1
    match char:
        case ">":
            if i % 2 != 0:
                santa_list[0] += 1
            if i % 2 == 0:
                r_santa_list[0] += 1
        case "<":
            if i % 2 != 0:
                santa_list[0] -= 1
            if i % 2 == 0:
                r_santa_list[0] -= 1
        case "^":
            if i % 2 != 0:
                santa_list[1] += 1
            if i % 2 == 0:
                r_santa_list[1] += 1
        case "v":
            if i % 2 != 0:
                santa_list[1] -= 1
            if i % 2 == 0:
                r_santa_list[1] -= 1
    if i % 2 != 0:
        coords.append((santa_list[0], santa_list[1]))
    if i % 2 == 0:
        coords.append((r_santa_list[0], r_santa_list[1]))
visited_at_least = len(set(coords))
print(f"on the second year Santa and Robo-Santa both visited: {visited_at_least}")
