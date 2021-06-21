# Group 1 - CDIO Project, 21-06-21

from boardfiller import boardfiller
from cardnormalizer import cardnormalizer
from duplicateremover import duplicateremover
from solitaireboardDTO import SolitaireBoardDTO


# gets a SolitaireBoard DTO, which is a way to display the location of the cards on the board.
def getboardDTO(json_results):

    board = SolitaireBoardDTO()

    # Remove all duplicate predictions, ensuring only the top left prediction of a card exists.
    # (and thereby removes the bottom right one)
    prunedtemplist = duplicateremover(json_results)

    # Normalize the position of the cards given the bounds of all cards location according to the boards bb.
    prunedtemplist = cardnormalizer(prunedtemplist)

    # Fills up the board with the given list of cards, at the correct locations.
    board = boardfiller(board, prunedtemplist)

    return board
