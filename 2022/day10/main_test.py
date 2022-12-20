import unittest
import main

class main_test(unittest.TestCase):

    def test_input_example_1(self):
        data = main.read_file("inputs/part1.example")
        self.assertEqual(13140, main.solve_part1(data))

    def test_input_example_2(self):
        data = main.read_file("inputs/part2.example")
        #data = main.read_file("inputs/part1.example")
        self.assertEqual(14720, main.solve_part2(data))
if __name__ == '__main__':
    unittest.main()
