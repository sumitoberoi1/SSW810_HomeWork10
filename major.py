class Major:
    def __init__(self,name):
        self.name = name
        self.required  = set()
        self.electives = set()

    def process_course(self,flag,course):
        if flag == "R":
            self.required.add(course)
        elif flag == "E":
            self.electives.add(course)
        else:
            raise ValueError('Invalid Flag')

    def update_grade_according_to_student_courses(self,student_courses):
        passing_grades = ('A', 'A-', 'B+', 'B', 'B-', 'C+', 'C') 
        completed_courses = []
        for course in student_courses:
            grade = student_courses[course]
            if grade in passing_grades:
                completed_courses.append(course)
        
        remaining_required_courses = []
        for course in self.required:
            if course not in completed_courses:
                remaining_required_courses.append(course)
        
        electives_left = []
        for course in self.electives:
            if course in completed_courses:
                electives_left = None
                break
            else:
                electives_left.append(course)

        if len(remaining_required_courses) == 0:
            remaining_required_courses = None

        return [sorted(completed_courses),remaining_required_courses,electives_left]
        

    def get_summary(self):
        return [self.name,sorted(list(self.required)),sorted(list(self.electives))]