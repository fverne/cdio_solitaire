from solitaire_card import SolitaireCard

# SolitaireBoard, keeps information about the state of the board
class SolitaireBoard:
    def __init__(self):
        self.bottom = list()
        self.left = SolitaireCard
        self.right = list()

    def addcard(self, pos, card):
        if pos == "left":
            self.left = card
        if pos == "right":
            self.right.append(card)
        if pos == "bottom":
            self.bottom.append(card)

