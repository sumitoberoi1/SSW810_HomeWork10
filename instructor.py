""" Instructor class containing details of particular instructor """
from collections import defaultdict
class Instructor:
    def __init__(self,info):
        """ Initializer for instuctor class """
        self.cwid = info.get('cwid')
        self.name = info.get('name')
        self.department = info.get('dept')
        self.courses = defaultdict(int)

    def increement_student_for_course(self,course):
        """ Add Course for a instructor """
        self.courses[course] += 1
    
    def get_summary(self):
        """ Get summary to print for PrettyTable """
        if len(self.courses) > 0:
            print_array = []
            for course in self.courses:
                print_array.append([self.cwid,self.name,self.department,course,self.courses[course]])
            return print_array
        else:
            raise ValueError('Not enough courses')