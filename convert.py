from boardfiller import boardfiller
from cardnormalizer import cardnormalizer
from duplicateremover import duplicateremover
from solitaireboardDTO import SolitaireBoardDTO


# gets a SolitaireBoard DTO, which is a way to display the location of the cards on the board.
def getboardDTO(json_results):
    print("start")

    board = SolitaireBoardDTO()

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
