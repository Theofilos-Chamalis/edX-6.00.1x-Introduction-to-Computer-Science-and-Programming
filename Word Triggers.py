# Enter your code for WordTrigger, TitleTrigger, 
# SubjectTrigger, and SummaryTrigger in this box
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