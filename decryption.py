from string import ascii_lowercase as lower, ascii_uppercase as upper, ascii_letters as both

def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    words = text.split(" ")
    for shift in range(26):
        coder = buildCoder(shift)
        if sum(isWord(wordList, applyCoder(word, coder)) for word in words) > len(words) / 2:
            return shift
    return 0
