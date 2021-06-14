# this method will map the bounding box of the cards to a new one,
# namely the one dictated by the bounding box of the cards.
# This ensures better predictions regardless of how zoomed or panned the camera is on the cards.

# Main method for this file, finds the boards bounds, and maps the bounding boxes to the new bounds
def cardnormalizer(prunedtemplist):
    boardbounds = findboardbounds(prunedtemplist)
    prunedtemplist = normalizecards(prunedtemplist, boardbounds)

    return prunedtemplist


# Finds the largest values of x1, x2, y1, y2, meaning the bounds for the entire board.
def findboardbounds(prunedtemplist):
    boardbounds = list()
    x1, y1, x2, y2 = 1.0, 1.0, 0.0, 0.0
    for obj in prunedtemplist:
        if obj.bb[0] < x1:
            x1 = obj.bb[0]
        if obj.bb[1] < y1:
            y1 = obj.bb[1]
        if obj.bb[2] > x2:
            x2 = obj.bb[2]
        if obj.bb[3] > y2:
            y2 = obj.bb[3]

    boardbounds.insert(0, x1)
    boardbounds.insert(1, y1)
    boardbounds.insert(2, x2)
    boardbounds.insert(3, y2)

    return boardbounds


# Normalizes the cards given the bounds for the board found above.
def normalizecards(prunedtemplist, boardbounds):

    # Method for normalizing
    def normalizevalue(val, min1, max1):
        return (val - min1) / (max1 - min1)

    for obj in prunedtemplist:
        obj.bb[0] = normalizevalue(obj.bb[0], boardbounds[0], boardbounds[2])
        obj.bb[1] = normalizevalue(obj.bb[1], boardbounds[1], boardbounds[3])
        obj.bb[2] = normalizevalue(obj.bb[2], boardbounds[0], boardbounds[2])
        obj.bb[3] = normalizevalue(obj.bb[3], boardbounds[1], boardbounds[3])

    return prunedtemplist

