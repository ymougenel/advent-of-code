import unittest
import main


class main_test(unittest.TestCase):

    def test_get_value(self):
        self.assertEqual(0, main.get_value([(50, 98, 2), (52, 50, 48)], 0))
        self.assertEqual(52, main.get_value([(50, 98, 2), (52, 50, 48)], 50))
        self.assertEqual(50, main.get_value([(50, 98, 2), (52, 50, 48)], 98))
        self.assertEqual(51, main.get_value([(50, 98, 2), (52, 50, 48)], 99))
        self.assertEqual(100, main.get_value([(50, 98, 2), (52, 50, 48)], 100))
    # def test_input_example_1(self):
    #     data = main.read_file("inputs/example1.txt")
    #     self.assertEqual(0, main.solve_part1(data))
    #
    # def test_input_example_2(self):
    #     data = main.read_file("inputs/example2.txt")
    #     self.assertEqual(0, main.solve_part2(data))


if __name__ == '__main__':
    unittest.main()
