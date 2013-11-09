def sqrt(a):
    def tryit(x):
        return 0.5 * (a/x + x)
    return fixedPoint(tryit, 0.0001)