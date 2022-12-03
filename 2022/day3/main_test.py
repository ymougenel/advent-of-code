import unittest
import main

class main_test(unittest.TestCase):

    def test_input_exemple_1(self):
        data = main.read_file("inputs/part1.example")
        self.assertEqual(157, main.solve_part1(data))

    def test_input_exemple_2(self):
        data = main.read_file("inputs/part2.example")
        data = main.read_file("inputs/part1.example")
        self.assertEqual(70, main.solve_part2(data))
if __name__ == '__main__':
    unittest.main()
