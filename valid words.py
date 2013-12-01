def isValidWord(word, hand, wordList):
    """
   Returns True if word is in the wordList and is entirely
   composed of letters in the hand. Otherwise, returns False.
 
   Does not mutate hand or wordList.
 
   word: string
   hand: dictionary (string -> int)
   wordList: list of lowercase strings
   """
    if word not in wordList:
        return False
    else:
        for i in word:
            if word.count(i) > hand.get(i, 0):
                return False
        return True