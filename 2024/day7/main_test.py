import unittest
import main


class main_test(unittest.TestCase):

    def test_input_example_1(self):
        data = main.read_file("inputs/example1.txt")
        self.assertEqual(3749, main.solve_part1(data))

    def test_generate_operations(self):
        self.assertCountEqual([[10, "+", 19], [10, "*", 19]], main.generate_operations([10, 19]))
        self.assertCountEqual(
            [[81, "+", 40, "+", 27], [81, "+", 40, "*", 27], [81, "*", 40, "+", 27], [81, "*", 40, "*", 27]],
            main.generate_operations([81, 40, 27]))

    def test_solf_operation(self):
        self.assertEqual(29, main.solve_operation([10, "+", 19]))
        self.assertEqual(190, main.solve_operation([10, "*", 19]))
        self.assertEqual(148, main.solve_operation([81, "+", 40, "+", 27]))
        self.assertEqual(3267, main.solve_operation([81, "*", 40, "+", 27]))
        self.assertEqual(87480, main.solve_operation([81, "*", 40, "*", 27]))
        self.assertEqual(3267, main.solve_operation([81, "+", 40, "*", 27]))
    # def test_input_example_2(self):
    #     data = main.read_file("inputs/example2.txt")
    #     self.assertEqual(0, main.solve_part2(data))

    def test_input_1(self):
        data = main.read_file("inputs/input.txt")
        self.assertEqual(1620690235709, main.solve_part1(data))

    # def test_input_2(self):
    #     data = main.read_file("inputs/input.txt")
    #     self.assertEqual(0, main.solve_part2(data))


if __name__ == '__main__':
    unittest.main()
