''' Shows result of creating differential between two pmf's.'''

import thinkbayes2
from thinkbayes2 import Suite, Pmf
import thinkplot


def main():
    die1 = thinkbayes2.Pmf()
    for x in [1, 2, 3, 4, 5, 6]:
        die1.Set(x, 1/6.0)

    die2 = thinkbayes2.Pmf()
    for x in [1, 2, 3, 4, 5, 6, 7, 8]:
        die2.Set(x, 1/8.0)

    diff = die2 - die1

    print(str(diff))


if __name__ == "__main__":
    main()
