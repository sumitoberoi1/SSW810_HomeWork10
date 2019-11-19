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
        self.assertEqual(repo.get_majors_details(),[['SFEN', ['SSW 810'], []]])
        self.assertEqual(repo.get_students_details()[0], ['10103', 'Jobs, S', 'SFEN', ['SSW 810'], None, []])

    def test_instructor_info(self):
        """Function to test instructors details """
        test_blank = "/Users/sumitoberoi/Documents/SSW-810/HW09/TestBlank"
        repo = Repository(test_blank)
        self.assertEqual(len(repo.get_instructors_details()),0)
        self.assertEqual(repo.get_instructors_details(),[])
        test_one_student = "/Users/sumitoberoi/Documents/SSW-810/HW09/TestOneStudent"
        repo = Repository(test_one_student)
        self.assertEqual(len(repo.get_instructors_details()),1)
        self.assertEqual(repo.get_instructors_details()[0],['98763', 'Cohen, R', 'SFEN', 'SSW 810', 1])

    def test_read_from_db(self):
        """ Method to test read from db """
        dir_path = "/Users/sumitoberoi/Documents/SSW-810/HW09/Stevens"
        db_path = "/Users/sumitoberoi/Documents/SSW-810/HW09/HW11.db"
        repo = Repository(dir_path)
        print("Res",repo.get_instructors_details_from_db(db_path))
        res_expected = [(98762, 'Hawking, S', 'CS', 'CS 501', 1), 
        (98762, 'Hawking, S', 'CS', 'CS 546', 1),
         (98762, 'Hawking, S', 'CS', 'CS 570', 1), (98763, 'Rowland, J', 'SFEN', 'SSW 555', 1),
          (98763, 'Rowland, J', 'SFEN', 'SSW 810', 4), 
          (98764, 'Cohen, R', 'SFEN', 'CS 546', 1)]
        self.assertEqual(repo.get_instructors_details_from_db(db_path), res_expected)



if __name__ == "__main__":
    unittest.main(exit=False,verbosity=2)  
