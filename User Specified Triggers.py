# Enter your code for makeTrigger in this box
def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.
 
    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")
 
    Modifies triggerMap, adding a new key-value pair for this trigger.
 
    Returns: None
    """
    # TODO: Problem 11
    if triggerType == "TITLE":
        triggerMap[name] = TitleTrigger(params[0])
 
    elif triggerType == "SUBJECT":
        triggerMap[name] = SubjectTrigger(params[0])
 
    elif triggerType == "SUMMARY":
        triggerMap[name] = SummaryTrigger(params[0])
 
    elif triggerType == "NOT":
        triggerMap[name] = NotTrigger(triggerMap[params[0]])
 
    elif triggerType == "AND":
        triggerMap[name] = AndTrigger(triggerMap[params[0]], triggerMap[params[1]])
 
    elif triggerType == "OR":
        triggerMap[name] = OrTrigger(triggerMap[params[0]], triggerMap[params[1]])
 
    elif triggerType == "PHRASE":
        triggerMap[name] = PhraseTrigger(' '.join(params))
 
    return triggerMap[name]