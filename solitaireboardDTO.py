from solitairecardDTO import SolitaireCardDTO


# SolitaireBoard, keeps information about the state of the board
class SolitaireBoardDTO:
    def __init__(self):
        self.left = SolitaireCardDTO
        self.right = list()
        for i in range(0, 4):
            self.right.append(None)
        self.bottom = list()
        for i in range(0, 7):
            self.bottom.append(list())

    def addcardleft(self, card):
        self.left = card

    def addcardright(self, card, stack):
        self.right[stack] = card

    def addcardbottom(self, card, stack):
        self.bottom[stack].append(card)


