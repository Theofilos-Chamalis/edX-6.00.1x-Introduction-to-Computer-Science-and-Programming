def flatten(aList):
    '''
    :param aList: a list
    :return: a copy of aList, which is a flattened version of aList
    '''
    flattened_list = [];

    for i in range(len(aList)):
        if isinstance(aList[i],list):
            flattened_list.extend(flatten(aList[i]));
        else:
            flattened_list.append(aList[i]);
    return flattened_list;