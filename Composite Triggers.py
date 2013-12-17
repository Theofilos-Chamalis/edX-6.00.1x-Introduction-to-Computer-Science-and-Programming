# Enter your code for WordTrigger, TitleTrigger,
# NotTrigger, AndTrigger, and OrTrigger in this box
class WordTrigger(Trigger):
 
    def __init__(self, word):
        self.word = word
        
    def isWordIn(self, text):
        text = [a.strip(string.punctuation).lower() for a in text.split(" ")]
        for word in text:
            if self.word.lower() in word.split("'"):
                return True
        return False
        
 
class TitleTrigger(WordTrigger):
 
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())
        
 
class SubjectTrigger(WordTrigger):
 
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())
 
 
class SummaryTrigger(WordTrigger):
 
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())
        
class NotTrigger(Trigger):
 
    def __init__(self, t1):
        self.t1 = t1
 
    def evaluate(self, story):
        return not self.t1.evaluate(story)
 
 
class AndTrigger(Trigger):
 
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2
 
    def evaluate(self, story):
        return self.t1.evaluate(story) and self.t2.evaluate(story)
 
        
class OrTrigger(Trigger):
 
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2
 
    def evaluate(self, story):
        return self.t1.evaluate(story) or self.t2.evaluate(story)