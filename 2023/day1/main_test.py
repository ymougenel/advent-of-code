import unittest
import main


class main_test(unittest.TestCase):

    def test_find_digit(self):
        self.assertEqual(1, main.read_digit("1abc2", True))
        self.assertEqual(2, main.read_digit("1abc2", False))
        self.assertEqual(3, main.read_digit("pqr3stu8vwx", True))
        self.assertEqual(8, main.read_digit("pqr3stu8vwx", False))
        self.assertEqual(7, main.read_digit("treb7uchet", True))
        self.assertEqual(7, main.read_digit("treb7uchet", False))

    def test_find_digit_with_letter(self):
        self.assertEqual(2, main.read_digit("two1nine", True, True))
        self.assertEqual(9, main.read_digit("two1nine", False, True))
        self.assertEqual(1, main.read_digit("abcone2threexyz", True, True))
        self.assertEqual(3, main.read_digit("abcone2threexyz", False, True))
        self.assertEqual(7, main.read_digit("7pqrstsixteen", True, True))
        self.assertEqual(6, main.read_digit("7pqrstsixteen", False, True))

    def test_input_example_1(self):
        data = main.read_file("inputs/part1.example")
        self.assertEqual(142, main.solve_part1(data))

    def test_input_example_2(self):
        data = main.read_file("inputs/part2.example")
        self.assertEqual(281, main.solve_part2(data))


if __name__ == '__main__':
    unittest.main()
