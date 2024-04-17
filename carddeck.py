import random
from card import Card

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards
    
    def shuffle(self):
        random.shuffle(self._cards)
    
    def draw(self):
        return self._cards.pop()
    
    # 'this' == 'self'
    def __str__(self):
        my_class = type(self)
        class_name = my_class.__name__
        return f"{class_name}:{len(self._cards)}"
    
    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}()"
    
    def __len__(self):
        return len(self._cards)

    @classmethod
    def get_suits(cls):
        return cls.SUITS    

    @staticmethod
    def bark(bark_type):
        print(f"{bark_type}! {bark_type}!")

if __name__ == "__main__":
    d1 = CardDeck()
    print(f"{d1 = }")
    print(d1)
    print(f"{d1.cards = }")
    d1.shuffle()
    for _ in range(5):
        card = d1.draw()
        print(card)

    print(f"{len(d1) = }")
    print(f"{d1.get_suits() = }")
    print(f"{CardDeck.get_suits() = }")
    d1.bark("woof")
    CardDeck.bark("arf")