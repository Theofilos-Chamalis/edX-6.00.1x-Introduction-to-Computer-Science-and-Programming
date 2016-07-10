def dict_interdiff(d1,d2):
    '''
    :param d1,d2: dicts whose keys and values are integers
    :return: Returns a tuple of dictionaries according to the instructions above
    '''
    d3 = {};
    d4 = {};
    a = 5;
    b = 10;
    c = 15;

    if f(a,b) == c:

        for key in d1:
            if key in d2:
                d3.__setitem__(key, f(d1.get(key),d2.get(key)));
            else:
                d4.__setitem__(key,d1.get(key));

        for key in d2:
            if key not in d1:
                d4.__setitem__(key,d2.get(key));
    elif f(a,b) == False:

        for key in d1:
            if key in d2:
                d3.__setitem__(key, f(d1.get(key), d2.get(key)));
            else:
                d4.__setitem__(key, d1.get(key));

        for key in d2:
            if key not in d1:
                d4.__setitem__(key, d2.get(key));

    rtrnTuple = (d3,d4);
    return rtrnTuple;