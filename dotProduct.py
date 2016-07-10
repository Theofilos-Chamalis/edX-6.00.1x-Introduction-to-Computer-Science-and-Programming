def dotProduct(listA, listB):
    '''
    :param listA: a list of numbers
    :param listB: a list of numbers of the same length as listA
    :return:
    '''
    dProd = 0;
    for i in range(0, len(listA)):
        dProd += listA[i] * listB[i];
    return dProd;