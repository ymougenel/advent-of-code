import unittest
import main

class main_test(unittest.TestCase):

    def test_input_example_1(self):
        data = main.read_file("inputs/example1.txt")
        self.assertEquals(2, main.solve_part(data))

    def test_increase_decrease_function(self):
        data = main.read_file("inputs/example1.txt")
        self.assertTrue(main.check_increase_decrease_range(data[0]))
        self.assertFalse(main.check_increase_decrease_range(data[1]))
        self.assertFalse(main.check_increase_decrease_range(data[2]))
        self.assertFalse(main.check_increase_decrease_range(data[3]))
        self.assertFalse(main.check_increase_decrease_range(data[4]))
        self.assertTrue(main.check_increase_decrease_range(data[5]))

    def test_input_part_1(self):
        data = main.read_file("inputs/input.txt")
        self.assertEqual(479, main.solve_part(data))

    def test_increase_decrease_function_tolerance(self):
        data = main.read_file("inputs/example1.txt")
        self.assertTrue(main.check_increase_decrease_range([1, 5, 2, 3], tolerate=1))
        self.assertTrue(main.check_increase_decrease_range([1, 3, 2, 3], tolerate=1))
        self.assertTrue(main.check_increase_decrease_range([1, 3, 1, 4], tolerate=1))
        self.assertTrue(main.check_increase_decrease_range([1, 3, 4, 9], tolerate=1))
        self.assertTrue(main.check_increase_decrease_range([5, 3, 4, 5], tolerate=1))

    def test_input_example_2(self):
        data = main.read_file("inputs/example1.txt")
        self.assertEqual(4, main.solve_part(data, tolerate=1))


if __name__ == '__main__':
    unittest.main()
