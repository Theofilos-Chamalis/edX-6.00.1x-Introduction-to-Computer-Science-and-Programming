def satisfiesF(L):
    '''
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
        that f(s) returns True, and no other elements. Remaining elements in L
        should be in the same order.
    :param L:
    :return: Returns the length of L after mutation
    '''
    falseCounter = 0;
    falseFlag = 0;
    falsePositions = [];

    for i in range(0, len(L)):
        if f(L[i]) == False:
            falseCounter += 1;
            falseFlag = 1;
            falsePositions.append(i);

    falsePositions.reverse();

    if falseFlag == 1:
        for i in range(0, falseCounter):
            L.__delitem__(falsePositions[i]);

    return len(L);

run_satisfiesF(L, satisfiesF)