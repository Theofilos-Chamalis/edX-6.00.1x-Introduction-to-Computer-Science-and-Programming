def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    join = []
    smaller = min(s1, s2, key=len)
    for num in range(len(smaller)):
        join.append(s1[num])
        join.append(s2[num])
    join = ''.join(join)
    if len(s1) != len(s2):
        smaller = len(smaller)
        join = join + max(s1, s2, key=len)[smaller:]
    return join