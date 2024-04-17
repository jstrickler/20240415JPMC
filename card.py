"""
One playing card

Usage:
Card('rank', 'suit')
"""
class Card: # inherits from 'object'
    def __init__(self, rank, suit):
        self._rank = rank   # "private" data
        self._suit = suit

    @property   # decorator
    def rank(self):   # getter property (cf. getter method)
        """
        Rank of this card
        """
        return self._rank

    @rank.setter
    def rank(self, value):
        """
        Suit of this card
        """
        if isinstance(value, str):
            self._rank = value
        else:
            raise TypeError("rank must be a str")

    @property
    def suit(self):
        return self._suit

    # human-friendly version of object
    def __str__(self):
        return f"{self.rank}-{self.suit}"

    # interpreter-friendly version
    def __repr__(self):
        return f'Card("{self.rank}", "{self.suit}")'

if __name__ == "__main__":
    c1 = Card('8', 'Diamonds')
    print(f"{c1 = }")
    print(c1)
    print(repr(c1))

    print(f"{c1.rank = }")
    print(f"{c1.suit = }")
    
    c1.rank = 'A'
    print(f"{c1.rank = }")
    print(c1)
    print(repr(c1))
#  print(x)     print(str(x))
#  f"{x = }"    repr(x)