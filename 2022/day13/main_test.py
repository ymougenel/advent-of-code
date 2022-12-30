import unittest
import main


class main_test(unittest.TestCase):

    def test_input_example_1(self):
        data = main.read_file("inputs/part1.example")
        self.assertEqual(13, main.solve_part1(data))

    def test_check_integers(self):
        self.assertEqual(-1, main.check_integers(5, 3))
        self.assertEqual(1, main.check_integers(5, 8))
        self.assertEqual(0, main.check_integers(5, 5))

    def test_check_list_int(self):
        self.assertEqual(1, main.check_list([1, 2, 3], [1, 2, 3, 4]))
        self.assertEqual(-1, main.check_list([1, 2, 3], [1, 2]))
        self.assertEqual(0, main.check_list([1, 2, 3], [1, 2, 3]))

        self.assertEqual(1, main.check_list([0, 1, 2], [1, 2, 3]))
        self.assertEqual(-1, main.check_list([0, 4, 2], [1, 2, 3]))
        self.assertEqual(1, main.check_list([1, 2, 3], [1, 3, 3]))
        self.assertEqual(1, main.check_list([1, 2, 3], [1, 3, 3]))
if __name__ == '__main__':
    unittest.main()
