from solitaire_card import SolitaireCard

# SolitaireBoard, keeps information about the state of the board
class SolitaireBoard:
    def __init__(self):
        self.left = SolitaireCard
        self.right = list()
        self.bottom = list()
        for i in range(0, 7):
            self.bottom.append(list())

    def addcardleft(self, card):
        self.left = card

    def addcardright(self, card, stack):
        self.right.insert(stack, card)

    def addcardbottom(self, card, stack):
        self.bottom[stack].append(card)


