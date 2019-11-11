""" Student class which contains details for particular student """
from collections import defaultdict
class Student:
    """ Student class which contains details for particular student """
    def __init__(self,info):
        """ Initializer for student """
        self.cwid = info.get('cwid')
        self.name = info.get('name')
        self.major = info.get('major')
        self.courses = defaultdict(str)
        
    def add_course(self,course_name,grade = None):
        """ Assign course to a student check if grade is there """
        if course_name in self.courses:
            raise ValueError ('Course already assigned to student')
        else:
            self.courses[course_name] = grade
        
    def get_summary(self):
        """ Get summary to print for PrettyTable """
        #Reference:  https://stackoverflow.com/questions/9001509/how-can-i-sort-a-dictionary-by-key
        return [self.cwid,self.name,self.major.name]

        



        
        

        
    