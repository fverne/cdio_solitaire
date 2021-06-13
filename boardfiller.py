# Takes a list of normalized cards and assigns them to a board DTO.
from solitaire_board import SolitaireBoard


def boardfiller(board: SolitaireBoard, prunedtemplist):
    for card in prunedtemplist:
        # Top cards
        if card.bb[1] <= 0.20:
            # top left card
            if card.bb[0] < 0.25:
                board.addcardleft(card)
                # print("added " + card.classname + " to left.")

            # top right cards
            if card.bb[0] > 0.90:
                board.addcardright(card, 3)
                # print("added " + card.classname + " to right 3.")
            elif card.bb[0] > 0.66:
                board.addcardright(card, 2)
                # print("added " + card.classname + " to right 2.")
            elif card.bb[0] > 0.49:
                board.addcardright(card, 1)
                # print("added " + card.classname + " to right 1.")
            elif card.bb[0] > 0.35:
                board.addcardright(card, 0)
                # print("added " + card.classname + " to right 0.")

        # Bottom Cards
        elif card.bb[1] > 0.2:
            if card.bb[0] > 0.92:
                board.addcardbottom(card, 6)
                # print("added " + card.classname + " to bottom 6.")
            elif card.bb[0] > 0.66:
                board.addcardbottom(card, 5)
                # print("added " + card.classname + " to bottom 5.")
            elif card.bb[0] > 0.49:
                board.addcardbottom(card, 4)
                # print("added " + card.classname + " to bottom 4.")
            elif card.bb[0] > 0.35:
                board.addcardbottom(card, 3)
                # print("added " + card.classname + " to bottom 3.")
            elif card.bb[0] > 0.21:
                board.addcardbottom(card, 2)
                # print("added " + card.classname + " to bottom 2.")
            elif card.bb[0] > 0.07:
                board.addcardbottom(card, 1)
                # print("added " + card.classname + " to bottom 1.")
            elif card.bb[0] <= 0.07:
                board.addcardbottom(card, 0)
                # print("added " + card.classname + " to bottom 0.")

    # Sorts the bottom cards given their Y-coordinates
    # First index is the most bottom card.
    for stack in board.bottom:
        def ycoordsorter(e):
            return e.bb[1]
        stack.sort(reverse=True, key=ycoordsorter)

    # debug
    # for list2 in board.bottom:
    #     for card in list2:
    #         print(card.classname)

    return board
