""" Repository class which contains details for a particular university like Stevens/NYU etc """
import os
import sqlite3
from student import Student
from instructor import Instructor
from prettytable import PrettyTable
from major import Major


class Repository:
    """Repository class which contains details for a particular university like Stevens/NYU etc """
    def __init__(self,dir_path):
        """ Initializer which reads from file and creates Student, Instructor and process Grades """
        self.students = []
        self.instructors = []
        try:
            file_path_for_student = os.path.join(dir_path,'students.txt')
            file_path_for_instructor = os.path.join(dir_path,'instructors.txt')
            file_path_for_majors = os.path.join(dir_path,'majors.txt')
        except FileNotFoundError as error:
            print(f"File Not Found {error}")
        else:
            self.majors = self.config_majors(file_path_for_majors)
            try:
                self.students = self.config_students(file_path_for_student)
            except ValueError as v_err:
                print(v_err)
            self.instructors = self.config_instructors(file_path_for_instructor)
            try:
                self.process_grades(dir_path)
            except ValueError as v_er:
                print(v_er)
            else:
                self.print_students_details()
                self.print_instructors_details()
                self.print_majors_details()
    
    def config_students(self,file_path_for_student):
        """ Creates Students from  students.txt """
        all_students = dict()
        for row_data in self.file_reading_gen(file_path_for_student,3,"\t",True):
            cwid, name, major = row_data
            if major not in self.majors:
                raise ValueError('Invalid Student and Major Combo')
            all_students[cwid] = Student({"cwid":cwid, "name":name,"major":self.majors[major]})
        return all_students

    def config_instructors(self,file_path_for_instructor):
        """ Creates Instructors from  instructors.txt """
        all_instructors = dict()
        for row_data in self.file_reading_gen(file_path_for_instructor,3,"\t",True):
            cwid, name, dept = row_data
            all_instructors[cwid] = Instructor({"cwid":cwid, "name":name,"dept":dept})
        return all_instructors


    def process_grades(self,dir_path):
        """ Processes grades and link courses to students and instructors """
        try:
            grades_path =  os.path.join(dir_path,'grades.txt')
        except FileNotFoundError as error:
            print(f"File Not Found {error}")
        else: 
            for student_id,course,grade,instructor_id in self.file_reading_gen(grades_path,4,"\t",True):
                if student_id not in self.students:
                    raise ValueError('Invalid Student')
                if instructor_id not in self.instructors:
                    raise ValueError('Invalid Instructor')
                student = self.students[student_id]
                student.add_course(course,grade)
                instructor = self.instructors[instructor_id]
                instructor.increement_student_for_course(course)


    def config_majors(self,majors_path):
        """ Process Majors """
        majors = dict()
        for major,flag,course in self.file_reading_gen(majors_path,3,"\t",True):
            if major not in majors:
                major_instance = Major(major)
                majors[major] = major_instance
            try:
                major_instance.process_course(flag,course)
            except ValueError as v_err:
                print(v_err)
        return majors

    def print_students_details(self):
        """ Prints Students Details in PrettyTable """
        table = PrettyTable(field_names=["CWID","Name","Major","Completed Courses","Remaining Required","Remaining Electives"])
        for row_info in self.get_students_details():
            table.add_row(row_info)
        print(table)

    def get_students_details(self):
        """ Creates students info to add to PrettyTable """
        row_infos = []
        for student_id in self.students:
            student = self.students[student_id]
            row_info = student.get_summary()
            row_info += student.major.update_grade_according_to_student_courses(student.courses)
            row_infos.append(row_info)
        return row_infos

    def get_majors_details(self):
        """ Creates majors info to add to PrettyTable """
        row_infos = []
        for major in self.majors:
            major_instance = self.majors[major]
            row_info = major_instance.get_summary()
            row_infos.append(row_info)
        return row_infos

    def get_instructors_details(self):
        """ Creates instructors info to add to PrettyTable """
        row_infos = []
        for instructor_id in self.instructors:
            instructor = self.instructors[instructor_id]
            if len(instructor.courses) > 0:
                instructor_rows = instructor.get_summary()
                for instructor_info in instructor_rows:
                    row_infos.append(instructor_info)
        return row_infos
        

    def print_instructors_details(self,db_path = None):
        """ Prints Instructors Details in PrettyTable """
        table = PrettyTable(field_names=["CWID","Name","Dept", "Course","Students"])
        if db_path is None:
            for row_info in self.get_instructors_details():
                table.add_row(row_info)
            print(table)
        else:
            for row_info in self.get_instructors_details_from_db(db_path):
                table.add_row(row_info)
            print(table)

    def print_majors_details(self):
        """ Prints Majors Details in PrettyTable """
        table = PrettyTable(field_names=["Major", "Required Courses", "Electives"])
        for row_info in self.get_majors_details():
            table.add_row(row_info)
        print(table)

    def file_reading_gen(self,path, fields, sep=',', header=False):
        """ Function tor creating generator to generate next line from CSV File """
        try:
            file = open(path)
        except FileNotFoundError:
            raise FileNotFoundError(f"Problem with reading file at path {path} ")
        else:
            with file:
                for line in file:
                    row_data = line.strip('\n').split(sep)
                    if len(row_data) != fields:
                        print(row_data)
                        raise ValueError(f"ValueError: {path} has {len(row_data)} expected {fields}")
                    else:
                        if header:
                            header = False
                            continue
                        else:
                            yield row_data

    def get_instructors_details_from_db(self,db_path):
        try:
            db = sqlite3.connect(db_path)
            row_infos = []
            query = """SELECT instructors.CWID,instructors.Name,instructors.Dept, grades.Course, COUNT(*) as NUM_OF_STUDENTS
                        FROM  instructors JOIN grades on CWID = InstructorCWID
                        Group By instructors.CWID, Course"""
            for row in db.execute(query):
                row_infos.append(row)
            db.close()
            return row_infos
        except sqlite3.OperationalError:
            raise sqlite3.OperationalError(f"There is some problem with your database Path {db_path}")

    def instructor_table_db(self, db_path):
        """ Read data from database mentioned in db_path """
        self.print_instructors_details(db_path)
        

def main():
    """ Main methods with Stevens Institute Processing """
    stevens_path = "/Users/sumitoberoi/Documents/SSW-810/HW09/Stevens"
    repo = Repository(stevens_path)
    db_path = "/Users/sumitoberoi/Documents/SSW-810/HW09/HW11.db"
    repo.instructor_table_db(db_path)

main()