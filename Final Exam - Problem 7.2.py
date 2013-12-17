def findFront(start):
    """
  start: a Frob that is part of a doubly linked list
  returns: the Frob at the beginning of the linked list
  """
    # Your Code Here
    if (start.getBefore()==None):
        return start
    else:
        return findFront(start.getBefore())