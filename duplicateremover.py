# Group 1 - CDIO Project, 21-06-21

from solitairecardDTO import SolitaireCardDTO


def duplicateremover(json_results):
    templist = list()

    # add the cards as objects to a temporary list
    for deck in json_results:
        for card in deck:
            templist.append(SolitaireCardDTO(card['class'], card['class_name'], card['normalized_box'],
                                             card['confidence']))

    # gets rid of duplicate entries, as these dont matter for the initial game state
    prunedtemplist = dict()
    for obj in templist:
        # add objects to temporary list if they dont exist
        if obj.classid not in prunedtemplist:
            prunedtemplist[obj.classid] = obj
        # if they do, and they are the "lowest" of the two bounding boxes, override its place with the highest one.
        elif prunedtemplist[obj.classid].bb[3] > obj.bb[3]:
            prunedtemplist[obj.classid] = obj

    templist = list(prunedtemplist.values())
    return templist

