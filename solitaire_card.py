
# SolitaireCard class, keeps information about a single card
class SolitaireCard:
    def __init__(self, classid: int, classname: str, bb: list, confidence: float):
        self.classid = classid
        self.classname = classname
        self.bb = bb
        self.confidence = confidence
