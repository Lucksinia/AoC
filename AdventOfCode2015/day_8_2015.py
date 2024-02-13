inpt = None
with open("AdventOfCode2015\тasks\8.txt") as f:
    inpt = f.read().splitlines()  # for no newline characters
    # part one: just character literals
print(first := sum(len(line) - len(eval(line)) for line in inpt))
# part two: only newly encoded strings
print(sum(line.count(r'"') + line.count("\\") + 2 for line in inpt))
