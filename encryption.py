from string import ascii_lowercase as lower, ascii_uppercase as upper, ascii_letters as both

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO 
    return dict(zip(both, (lower[shift:] + lower[:shift] + upper[shift:] + upper[:shift])))