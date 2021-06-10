
# check if three instances of a card appears (max 2 should be allowed
def checkcardsoverflow(json_results):
    cardsondeck = [0 for _ in range(52)]

    for deck in json_results:
        for card in deck:
            if cardsondeck[card['class']]:
                cardsondeck[card['class']].append(card['class'])
                if len(cardsondeck[card['class']]) > 2:
                    print("Something is wrong - got more than two objects of the same class")
                    return False
            else:
                cardsondeck[card['class']] = list()
                cardsondeck[card['class']].append(card['class'])
                print(card['class_name'] + " , " + str(card['confidence']))

    return True


