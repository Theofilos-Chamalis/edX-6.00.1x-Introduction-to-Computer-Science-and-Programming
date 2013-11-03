def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    L2 = []
    import string
    for c in string.ascii_lowercase:
        L2.append(c)
        #print L2
        
    def removeDupsBetter(L1,L2):
        L1Start = L1[:]
        for e in L1Start:
            if e in L2:
                L2.remove(e)
        return ''.join(str(e) for e in L2)
    
    return removeDupsBetter(lettersGuessed,L2)