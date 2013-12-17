def insert(atMe, newFrob):
    """
   atMe: a Frob that is part of a doubly linked list
   newFrob:  a Frob with no links 
   This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
   """
   
    #NewFrob comes before atMe.
    if newFrob.name < atMe.name:
        if atMe.before != None and atMe.before == newFrob.before:
            newFrob.after = atMe
            atMe.before = newFrob
            newFrob.before.after = newFrob
        elif atMe.before == None:
            atMe.before = newFrob
            newFrob.after = atMe
        else:
            newFrob.after = atMe
            insert(atMe.before, newFrob)
    #NewFrob comes after atMe.    
    elif newFrob.name > atMe.name:
        if atMe.after != None and atMe.after == newFrob.after:
            newFrob.before = atMe
            atMe.after = newFrob
            newFrob.after.before = newFrob
        elif atMe.after == None:
            atMe.after = newFrob
            newFrob.before = atMe
        else:
            newFrob.before = atMe
            insert(atMe.after, newFrob)
 
    #NewFrob has the same name as atMe.
    else:
        newFrob.after = atMe.after
        atMe.after = newFrob
        newFrob.before = atMe
        if newFrob.after != None:
            newFrob.after.before = newFrob