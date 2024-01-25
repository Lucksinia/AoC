"""
--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

    turn on 0,0 through 999,999 would turn on (or leave on) every light.
    toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
    turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

After following the instructions, how many lights are lit?
"""


def parse_line(line):
    words = line.split()
    x1, y1 = map(int, words[-3].split(","))
    x2, y2 = map(int, words[-1].split(","))
    return words[len(words) == 5], range(x1, x2 + 1), range(y1, y2 + 1)


def solve(data, grid_size=range(1000)):
    grid1 = [[0 for _ in grid_size] for _ in grid_size]
    grid2 = [[0 for _ in grid_size] for _ in grid_size]
    for cmd, xs, ys in data:
        for x in xs:
            for y in ys:
                if cmd == "on":
                    grid1[x][y] = 1
                    grid2[x][y] += 1
                elif cmd == "off":
                    grid1[x][y] = 0
                    grid2[x][y] = max(0, grid2[x][y] - 1)
                else:
                    grid1[x][y] = 1 - grid1[x][y]
                    grid2[x][y] += 2
    return sum(map(sum, grid1)), sum(map(sum, grid2))


data = map(parse_line, open("AdventOfCode2015/tasks/6.txt").read().splitlines())
print(solve(data))
