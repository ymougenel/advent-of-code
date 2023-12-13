import unittest
import main


class main_test(unittest.TestCase):
    # ???..????# 1,3,1

    def test_parse_opti_springs(self):
        self.assertEqual([".#"], main.parse_opti_springs(".?", [1], 1, 0))
        self.assertEqual(["..#", "#.."], main.parse_opti_springs("?.?", [1], 1, 0))
        self.assertEqual(['.#..##', '.#.##.', '#...##', '#..##.'], main.parse_opti_springs("??.?#?", [1, 2], 3, 1))
        self.assertEqual(['.#.###.#.######'], main.parse_opti_springs("?#?#?#?#?#?#?#?", [1, 3, 1, 6], 11, 7))
        # self.assertEqual(1, len(main.parse_opti_springs("?#?#?#?#?#?#?#?", [1, 3, 1, 6], 11, 7)))
    # def test_is_possible(self):
    #     """  ???..????# 1,3,1 """
    #     self.assertEqual(True, main.is_possibility("#...###.#", [1, 3, 1]))
    #     self.assertEqual(True, main.is_possibility(".#..###.#", [1, 3, 1]))
    #     self.assertEqual(True, main.is_possibility("..#.###.#", [1, 3, 1]))
    #     self.assertEqual(False, main.is_possibility("##..###.#", [1, 3, 1]))
    #
    #     """ ??.?#?"""
    #     self.assertEqual(True, main.is_possibility("#..##.", [1, 2]))
    #     self.assertEqual(True, main.is_possibility(".#.##.", [1, 2]))
    #     self.assertEqual(True, main.is_possibility("#...##", [1, 2]))
    #     self.assertEqual(True, main.is_possibility(".#..##", [1, 2]))
    #     self.assertEqual(False, main.is_possibility("##.##.", [1, 2]))
    #     self.assertEqual(False, main.is_possibility("...##.", [1, 2]))
    #     self.assertEqual(False, main.is_possibility(".#.###", [1, 2]))
    #
    # def test_input_example_1(self):
    #     data = main.read_file("inputs/example1.txt")
    #     data = [main.parse_springs(line) for line in data]
    #     self.assertEqual(21, main.solve_part1(data))
    #
    #
    # def test_input_part_1(self):
    #     data = main.read_file("inputs/input.txt")
    #     data = [main.parse_springs(line) for line in data]
    #     self.assertEqual(7191, main.solve_part1(data))
    #
    # def test_input_example_2(self):
    #     data = main.read_file("inputs/example2.txt")
    #     self.assertEqual(0, main.solve_part2(data))


if __name__ == '__main__':
    unittest.main()
