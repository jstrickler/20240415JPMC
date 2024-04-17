from card import Card
from carddeck import CardDeck

class Game:
    def play(self):
        print("Playing...")

class JokerDeck(Game, CardDeck):
    def _make_deck(self):
        super()._make_deck()
        for joker in range(1,3):
            card = Card(f"JOKER{joker}", f"JOKER{joker}")
            self._cards.append(card)

if __name__ == "__main__":
    j = JokerDeck()
    j.shuffle()
    for _ in range(10):
        print(j.draw())
    j.play()
    print(j)
    print(repr(j))