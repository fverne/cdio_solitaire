from boardfiller import boardfiller
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


# gets a SolitaireBoard DTO, which is a way to display the location of the cards on the board.
def getboard(json_results):
    print("start")

    board = SolitaireBoard()

    # Remove all duplicate predictions, ensuring only the top left prediction of a card exists.
    # (and thereby removes the bottom right one)
    prunedtemplist = duplicateremover(json_results)

    # Normalize the position of the cards given the bounds of all cards location according to the boards bb.
    prunedtemplist = cardnormalizer(prunedtemplist)

    # Fills up the board with the given list of cards, at the correct locations.
    board = boardfiller(board, prunedtemplist)

    return board

    # check if there are cards left in the list after extracting - there should be 7 max!
    # if len(prunedtemplist) > 0:
    #     print("more cards left after init finished! Something is wrong!")
