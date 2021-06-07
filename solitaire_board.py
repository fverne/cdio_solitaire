from solitaire_card import SolitaireCard

# SolitaireBoard, keeps information about the state of the board
class SolitaireBoard:
    def __init__(self):
        self.bottom = list()
        self.left = SolitaireCard
        self.right = list()

    def addcard(self, pos, card):
        if pos == 1:
            self.left = card
        if pos == 2:
            self.right.append(card)
        if pos == 3:
            self.bottom.append(card)

