import unittest
import main


class main_test(unittest.TestCase):

    def test_input_example_1(self):
        data = main.read_file("inputs/example1.txt")
        # self.assertEqual(2, main.solve_part1(data))

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
        self.assertEqual(479, main.solve_part1(data))


    # def test_input_example_2(self):
    #     data = main.read_file("inputs/example2.txt")
    #     self.assertEqual(0, main.solve_part2(data))


if __name__ == '__main__':
    unittest.main()
