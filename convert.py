import json

from solitaire_board import SolitaireBoard
from solitaire_card import SolitaireCard


#class which will convert a json object to another json object, used by the backend
def json_to_solitaire(json_results):
    board = SolitaireBoard()

    for deck in json_results:
        for card in deck:
            if board.left:
                board.addcard(1, SolitaireCard(card['class'], card['class_name'], card['normalized_box'],
                                           card['confidence']))

            if len(board.right) < 4:
                board.addcard(2, SolitaireCard(card['class'], card['class_name'], card['normalized_box'],
                                            card['confidence']))

            if len(board.bottom) < 7:
                board.addcard(3, SolitaireCard(card['class'], card['class_name'], card['normalized_box'],
                                            card['confidence']))

    return len(board.right)
