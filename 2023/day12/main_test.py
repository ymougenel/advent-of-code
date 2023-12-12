import unittest
import main


class main_test(unittest.TestCase):
    # ???..????# 1,3,1

    def test_is_possible(self):
        """  ???..????# 1,3,1 """
        self.assertEqual(True, main.is_possibility("#...###.#", [1, 3, 1]))
        self.assertEqual(True, main.is_possibility(".#..###.#", [1, 3, 1]))
        self.assertEqual(True, main.is_possibility("..#.###.#", [1, 3, 1]))
        self.assertEqual(False, main.is_possibility("##..###.#", [1, 3, 1]))

        """ ??.?#?"""
        self.assertEqual(True, main.is_possibility("#..##.", [1, 2]))
        self.assertEqual(True, main.is_possibility(".#.##.", [1, 2]))
        self.assertEqual(True, main.is_possibility("#...##", [1, 2]))
        self.assertEqual(True, main.is_possibility(".#..##", [1, 2]))
        self.assertEqual(False, main.is_possibility("##.##.", [1, 2]))
        self.assertEqual(False, main.is_possibility("...##.", [1, 2]))
        self.assertEqual(False, main.is_possibility(".#.###", [1, 2]))

    def test_input_example_1(self):
        data = main.read_file("inputs/example1.txt")
        data = [main.parse_springs(line) for line in data]
        self.assertEqual(21, main.solve_part1(data))


    def test_input_part_1(self):
        data = main.read_file("inputs/input.txt")
        data = [main.parse_springs(line) for line in data]
        self.assertEqual(7191, main.solve_part1(data))
    #
    # def test_input_example_2(self):
    #     data = main.read_file("inputs/example2.txt")
    #     self.assertEqual(0, main.solve_part2(data))


if __name__ == '__main__':
    unittest.main()
