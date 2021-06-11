from cardnormalizer import cardnormalizer
from duplicateremover import duplicateremover
from solitaire_board import SolitaireBoard
from solitaire_card import SolitaireCard


# class which will convert a json object to another json object, used by the backend
def json_to_solitaire(json_results):
    board = SolitaireBoard()

    for deck in json_results:
        for card in deck:
            if board.left:
                board.addcardleft(SolitaireCard(card['class'], card['class_name'], card['normalized_box'],
                                           card['confidence']))

            if len(board.right) < 4:
                board.addcardright(SolitaireCard(card['class'], card['class_name'], card['normalized_box'],
                                            card['confidence']), 1)

            board.addcardbottom(SolitaireCard(card['class'], card['class_name'], card['normalized_box'],
                                            card['confidence']), 1)

    return board


# starts the game with a given uid, and keeps the state.
def getboard(json_results):
    print("start")

    board = SolitaireBoard()

    # Remove all duplicate predictions, ensuring only the top left prediction of a card exists.
    # (and thereby removes the bottom right one)
    prunedtemplist = duplicateremover(json_results)

    # Normalize the position of the cards given the bounds of all cards location according to the boards bb.
    prunedtemplist = cardnormalizer(prunedtemplist)

    # finds the card in the top-left corner
    topcard = None
    tempbb = 0.0
    for obj in prunedtemplist:
        if obj.bb[3] > tempbb:
            topcard = obj
            tempbb = obj.bb[3]

    print("topcard " + topcard.classname)
    # adds the card to the top-left border in the board object
    board.addcardleft(topcard)
    prunedtemplist.remove(topcard)

    # adds the cards to the bottom lists
    leftmostcard = SolitaireCard
    tempbb = 1.0
    for i in range(0, 7):
        for obj in prunedtemplist:
            if tempbb > obj.bb[1]:
                leftmostcard = obj
                tempbb = obj.bb[1]
        tempbb = 1.0
        board.addcardbottom(leftmostcard, i)
        print(leftmostcard.classname)
        prunedtemplist.remove(leftmostcard)

    # check if there are cards left in the list after extracting - there should be 7 max!
    if len(prunedtemplist) > 0:
        print("more cards left after init finished! Something is wrong!")
