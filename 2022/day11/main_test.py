import unittest
import main

class main_test(unittest.TestCase):

    def test_input_example_1(self):
        data = main.read_file("inputs/part1.example")

        self.assertEqual(10605, main.solve_part1(data))

    def test_input_input1(self):
        data = main.read_file("inputs/part1.input")
        self.assertEqual(76728, main.solve_part1(data))
if __name__ == '__main__':
    unittest.main()
