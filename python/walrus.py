# When to use Walrus operator?
# When the output of a function or a method needs to be checked in a condition and saved for later.
# Calling function/method twice would not be effective.
# Introducing a variable before if statement would mean the variable lingers after if-branch is resolved.

import random


class BasicDemo:
    """Basic demo for Walrus operator
    If get_ones returns a list that is not empty, print it.
    Otherwise report that the list is empty.
    """
    def __init__(self):
        pass

    def get_ones(self):
        return [1 for _ in range(random.randint(0, 2))]

    def run(self):
        if (ones := self.get_ones()):
            print(ones)
        else:
            print("There is no one")


class UniqueInOrder:
    """UniqueInOrder one-liner (https://www.codewars.com/)
    transform("AAAABBBCCDAABBB") -> ["A", "B", "C", "D", "A", "B"]
    transform("ABBCcAD")         -> ["A", "B", "C", "c", "A", "D"]
    transform([1, 2, 2, 3, 3])   -> [1, 2, 3]
    transform((1, 2, 2, 3, 3))   -> [1, 2, 3]
    """
    def __init__(self):
        pass

    @staticmethod
    def transform(sequence):
        return [previous := sequence[0] if sequence else None] + [previous := item for item in sequence if previous != item]

    def run(self):
        print(self.transform("AAAABBBCCDAABBB"))
        print(self.transform("ABBCcAD"))
        print(self.transform([1, 2, 2, 3, 3]))
        print(self.transform((1, 2, 2, 3, 3)))
        print(self.transform(""))


def main():
    print("Walrus operator demo")

    bd = BasicDemo()
    bd.run()

    uio = UniqueInOrder()
    uio.run()


if __name__ == "__main__":
    main()
