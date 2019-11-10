class Major:
    def __init__(self,name,required=set(),electives=set()):
        self.name = name
        self.required  = required
        self.electives = electives

    def process_course(self,flag,course):
        if flag == "R":
            self.required.add(course)
        elif flag == "E":
            self.electives.add(course)
        else:
            raise ValueError('Invalid Flag')

    def get_summary(self):
        return [self.name,sorted(list(self.required)),sorted(list(self.electives))]