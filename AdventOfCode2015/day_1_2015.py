"""
Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

For example:

    (()) and ()() both result in floor 0.
    ((( and (()(()( both result in floor 3.
    ))((((( also results in floor 3.
    ()) and ))( both result in floor -1 (the first basement level).
    ))) and )())()) both result in floor -3.

To what floor do the instructions take Santa?
"""

# ! all Advent of Code will be done with standatrt python libraries (My current python version => 3.11.0 )
# ? 1.txt is input file from task

floor = 0
with open("AdventOfCode2015/tasks/1.txt", "r") as f:
    bfs = f.read()
    for char in bfs:
        match char:
            case "(":
                floor += 1
            case ")":
                floor -= 1
    print(f"Santa got to the {floor} floor")

"""--- Part Two ---

Now, given the same instructions, find the position of the first character that causes
him to enter the basement (floor -1). The first character in the instructions has
position 1, the second character has position 2, and so on.

For example:

    ) causes him to enter the basement at character position 1.
    ()()) causes him to enter the basement at character position 5.

What is the position of the character that causes Santa to first enter the basement?
"""
floor = 0
count = 1
for char in bfs:
    match char:
        case "(":
            floor += 1
        case ")":
            floor -= 1
    if floor == -1:
        print(f"Santa arived at the basement! it took him {count} floors!")
        break
    count += 1
