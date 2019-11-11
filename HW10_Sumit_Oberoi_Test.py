import unittest
from repository import Repository

""" Test class for printable output in PrettyTable """
class TestRepository(unittest.TestCase):
    """ Test class for printable output in PrettyTable """

    def test_student_info(self):
        """Function to test students details """
        test_blank = "/Users/sumitoberoi/Documents/SSW-810/HW09/TestBlank"
        repo = Repository(test_blank)
        self.assertEqual(len(repo.get_students_details()),0)
        self.assertEqual(repo.get_students_details(),[])
        self.assertEqual(repo.get_majors_details(),[])
        test_one_student = "/Users/sumitoberoi/Documents/SSW-810/HW09/TestOneStudent"
        repo = Repository(test_one_student)
        self.assertEqual(len(repo.get_students_details()),1)
        self.assertEqual(repo.get_majors_details(),[['SFEN', ['SSW 540'], ['CS 501']]])
        self.assertEqual(repo.get_students_details()[0],['10103', 'Baldwin, C', 'SFEN', ['SSW 540'], None, ['CS 501']])

    def test_instructor_info(self):
        """Function to test instructors details """
        test_blank = "/Users/sumitoberoi/Documents/SSW-810/HW09/TestBlank"
        repo = Repository(test_blank)
        self.assertEqual(len(repo.get_instructors_details()),0)
        self.assertEqual(repo.get_instructors_details(),[])
        test_one_student = "/Users/sumitoberoi/Documents/SSW-810/HW09/TestOneStudent"
        repo = Repository(test_one_student)
        self.assertEqual(len(repo.get_instructors_details()),1)
        self.assertEqual(repo.get_instructors_details()[0],['98765', 'Einstein, A', 'SFEN', 'SSW 540', 1])



if __name__ == "__main__":
    unittest.main(exit=False,verbosity=2)  
