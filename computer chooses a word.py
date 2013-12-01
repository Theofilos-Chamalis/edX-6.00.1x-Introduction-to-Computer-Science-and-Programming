def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    bestScore = 0

    bestWord = None

    for word in wordList:

        if isValidWord(word, hand, wordList):

            score = getWordScore(word, n)

            if score > bestScore:

                bestScore = score
                bestWord = word

    return bestWord