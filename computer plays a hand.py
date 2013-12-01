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

def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is
    displayed, the remaining letters in the hand are displayed, and the
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    def displayHand2(hand):
      displayed = ''
      for letter in hand.keys():
        for j in range(hand[letter]):
             displayed += letter + ' '
      return displayed
    totalScore = 0
    handed = hand.copy()
    while compChooseWord(handed, wordList, n):
        print "Current Hand:  " + displayHand2(handed)
        askInput = compChooseWord(handed, wordList, n)
        scored = getWordScore(askInput, n)
        totalScore += scored
        print '"'+ askInput + '" ' + "earned " + str(scored) + " points. Total: " + str(totalScore) + " points\n"
        handed = updateHand(handed, askInput)
    if sum(handed.values()) != 0:
      print "Current Hand:  " + displayHand2(handed)
    print "Total score: " + str(totalScore) + " points"
