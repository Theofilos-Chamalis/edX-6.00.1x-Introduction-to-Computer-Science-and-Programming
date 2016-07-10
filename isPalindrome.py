def isPalindrome(aString):
    '''
    :param aString: a string
    '''
    for i in range (0, (len(aString)+1)/2):
        if aString[-i-1] != aString[i]:
            return False;
    return True;
