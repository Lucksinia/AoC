"""--- Day 7: Some Assembly Required ---

This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! 
Unfortunately, little Bobby is a little under the recommended age range, and he 
needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal 
(a number from 0 to 65535). A signal is provided to each wire by a gate, another wire,
or some specific value. Each wire can only get a signal from one source, but can provide
its signal to multiple destinations. A gate provides no signal until all of its inputs
have a signal.

The included instructions booklet describes how to connect the parts together: 
x AND y -> z means to connect wires x and y to an AND gate, and then connect 
its output to wire z.

For example:

    123 -> x means that the signal 123 is provided to wire x.
    x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
    p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
    NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason,
you'd like to emulate the circuit instead, almost all programming languages 
(for example, C, JavaScript, or Python) provide operators for these gates.

In little Bobby's kit's instructions booklet (provided as your puzzle input),
what signal is ultimately provided to wire a?
"""
from operator import lshift, rshift, and_, or_
from functools import cache


def parse(table, val="a", b=None) -> int:
    operations = {"AND": and_, "OR": or_, "LSHIFT": lshift, "RSHIFT": rshift}

    # as we cant cache dicts, here is very dishonorable hack
    @cache
    def cashed_op(val):
        try:
            return int(val)
        except ValueError:
            path = table[val]
            match len(path):
                case 1:
                    return cashed_op(path[0])
                case 2:
                    return ~cashed_op(path[1]) & 0xFFFF
                case 3:
                    return operations[path[1]](cashed_op(path[0]), cashed_op(path[2]))

    if b is not None:
        table["b"] = [b]
    return cashed_op(val)


with open("AdventOfCode2015/tasks/7.txt") as f:
    inpt = f.read().splitlines()
    parse_input = lambda inpt: {
        (s := line.split(" -> "))[1]: s[0].split() for line in inpt
    }
    table = parse_input(inpt)
print(
    second := parse(table, "a")
)  # walrus operator is used to assign values *inside* expressions. I didn't  know it yet
print(parse(table, "a", second))  # part two
