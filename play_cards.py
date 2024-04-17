from carddeck import CardDeck

c = CardDeck()

c.shuffle()

for _ in range(10):
    print(c.draw())