 # Paste your code into this box
def find(s, sub):
    counter = start = 0
    while True:
        start = s.find(sub, start) + 1
        if start > 0:
            counter+=1
        else:
            return counter
print find(s,'bob');