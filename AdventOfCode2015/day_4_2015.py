"""
--- Day 4: The Ideal Stocking Stuffer ---

Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

    If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
    If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....

"""

from itertools import count
from functools import cache  # just for speed
from hashlib import md5

f = open("AdventOfCode2015/tasks/4.txt", "r")
hash = str(f.read())
f.close()


@cache
def minting(hash: str, zeroes: str) -> int:
    for x in count(start=0, step=1):
        res = md5(f"{hash}{x}".encode("utf-8")).hexdigest()
        if res.startswith(zeroes):
            return x


print(f'with at least 5 zeroes: {minting(hash, "00000")}')

"""
--- Part Two ---
Now find one that starts with six zeroes.
"""

print(f"with at least 6 zeroes:", minting(hash, "000000"))

"""
? timeit results on time.process_time for funzies:
5 zeroes ~> 0.37 seconds
6 zeroes ~> 11 seconds
* with lru_cache:
5 zeroes => 0.0625 second
6 zeroes ~> 1 second
"""
