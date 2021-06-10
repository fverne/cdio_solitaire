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
def initializegame(json_results, uid):
    print("start")

    templist = list()
    board = SolitaireBoard()

    # add the cards as objects to a temporary list
    for deck in json_results:
        for card in deck:
            templist.append(SolitaireCard(card['class'], card['class_name'], card['normalized_box'],
                                           card['confidence']))

    # gets rid of duplicate entries, as these dont matter for the initial game state
    prunedtemplist = dict()
    for obj in templist:
        # add objects to temporary list if they dont exist
        if obj.classid not in prunedtemplist:
            prunedtemplist[obj.classid] = obj
        # if they do, and they are the "lowest" of the two bounding boxes, override its place with the highest one.
        elif prunedtemplist[obj.classid].bb[2] < obj.bb[2]:
            prunedtemplist[obj.classid] = obj

    # convert the dict to a list
    prunedtemplist = list(prunedtemplist.values())

    # finds the card in the top-left corner
    topcard = None
    tempbb = 0.0
    for obj in prunedtemplist:
        if obj.bb[2] > tempbb:
            topcard = obj
            tempbb = obj.bb[2]

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
