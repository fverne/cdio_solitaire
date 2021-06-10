from solitaire_board import SolitaireBoard


class SolitaireGame:
    uid = None
    board = None
    turn = int
    lastturn = int

    def __init__(self, uid: str, board: SolitaireBoard):
        self.uid = uid
        self.board = board
        self.turn = 0
        self.lastturn = 0
