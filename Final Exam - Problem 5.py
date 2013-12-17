class edx(object):
    def __init__(self, courses):
        self.myCourses = []
        for course in courses:
            self.myCourses.append(courseInfo(course))
 
    def setGrade(self, grade, course="6.01x"):
        """
       grade: integer greater than or equal to 0 and less than or equal to 100
       course: string
 
       This method sets the grade in the courseInfo object named by `course`.  
 
       If `course` was not part of the initialization, then no grade is set, and no
       error is thrown.
 
       The method does not return a value.
       """
        #   fill in code to set the grade
 
        for c in self.myCourses:
            if c.courseName == course:
                c.setGrade( grade)
       
 
    def getGrade(self, course="6.02x"):
        """
       course: string
 
       This method gets the grade in the the courseInfo object named by `course`.
 
       returns: the integer grade for `course`.  
       If `course` was not part of the initialization, returns -1.
       """
        #   fill in code to get the grade
        for c in self.myCourses:
            if c.courseName == course:
                return c.getGrade()
       
        return -1
 
    def setPset(self, pset, score, course="6.00x"):
        """
       pset: a string or a number
       score: an integer between 0 and 100
       course: string
 
       The `score` of the specified `pset` is set for the
       given `course` using the courseInfo object.
 
       If `course` is not part of the initialization, then no pset score is set,
       and no error is thrown.
       """
        for i in range(len(self.myCourses)):
            if self.myCourses[i].courseName == course:
                self.myCourses[i].setPset( pset, score)
       
 
    def getPset(self, pset, course="6.00x"):
        """
       pset: a string or a number
       score: an integer between 0 and 100
       course: string        
 
       returns: The score of the specified `pset` of the given
       `course` using the courseInfo object.
       If `course` was not part of the initialization, returns -1.
       """
        for c in self.myCourses:
            if c.courseName == course:
                return c.getPset(pset)        
        return -1