import unittest
import main

class main_test(unittest.TestCase):

    def test_input_example_1(self):
        data = main.read_file("inputs/example1.txt")
        self.assertEqual(140, main.solve_part1(data))

    def test_input_example_2(self):
        data = main.read_file("inputs/example2.txt")
        self.assertEqual(772, main.solve_part1(data))

    def test_input_example_3(self):
        data = main.read_file("inputs/example3.txt")
        self.assertEqual(1930, main.solve_part1(data))


    # def test_input_example_2(self):
    #     data = main.read_file("inputs/example2.txt")
    #     self.assertEqual(0, main.solve_part2(data))

    # def test_input_1(self):
    #     data = main.read_file("inputs/input.txt")
    #     self.assertEqual(186175, main.solve_part1(data))

    # def test_input_2(self):
    #     data = main.read_file("inputs/input.txt")
    #     self.assertEqual(0, main.solve_part2(data))

if __name__ == '__main__':
    unittest.main()
