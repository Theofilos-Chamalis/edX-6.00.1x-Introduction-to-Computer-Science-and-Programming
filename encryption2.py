from string import ascii_lowercase as lower, ascii_uppercase as upper, ascii_letters as both

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO
    return "".join([coder.get(letter, letter) for letter in text])