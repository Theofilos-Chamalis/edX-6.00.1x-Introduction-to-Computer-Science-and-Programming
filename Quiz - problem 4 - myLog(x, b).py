def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    assert(x > 0), "x is a positive integer !!!"
    assert(b>=2), "b is a positive integer >=2 !!!"
    count = -1;
    while x > 0:
        x /= b
        count += 1
        if x == 0:
            return count;
