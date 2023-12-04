import unittest
import main


class main_test(unittest.TestCase):

    def test_detect_number(self):
        data = main.read_file("inputs/example1.txt")
        self.assertEqual('467', main.detect_number(data, 0, 0))
        main.processed = []
        self.assertEqual('467', main.detect_number(data, 0, 1))
        main.processed = []
        self.assertEqual('467', main.detect_number(data, 0, 2))
        main.processed = []
        self.assertEqual('', main.detect_number(data, 1, 2))
        main.processed = []
        self.assertEqual('', main.detect_number(data, 1, 3))

    def test_input_example_1(self):
        data = main.read_file("inputs/example1.txt")
        self.assertEqual(4361, main.solve_part1(data))

    def test_input_example_2(self):
        data = main.read_file("inputs/example1.txt")
        main.processed = []
        self.assertEqual(467835, main.solve_part2(data))


if __name__ == '__main__':
    unittest.main()
