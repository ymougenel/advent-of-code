import unittest
import main


class main_test(unittest.TestCase):

    # def test_strength_part1(self):
    #     self.assertEqual(1, main.get_strength([1, 2, 3, 4, 5]))
    #     self.assertEqual(2.25, main.get_strength([1, 1, 3, 4, 5]))
    #     self.assertEqual(2.5, main.get_strength([1, 1, 4, 4, 5]))
    #     self.assertEqual(3, main.get_strength([4, 1, 4, 4, 5]))
    #     self.assertEqual(3.25, main.get_strength([4, 5, 4, 4, 5]))
    #     self.assertEqual(4, main.get_strength([4, 5, 4, 4, 4]))
    #     self.assertEqual(5, main.get_strength([6, 6, 6, 6, 6]))

    def test_strength_part1(self):
        main.part1 = False
        # without Joler (0), no difference
        self.assertEqual(1, main.get_strength([1, 2, 3, 4, 5]))
        self.assertEqual(2, main.get_strength([1, 1, 3, 4, 5]))
        self.assertEqual(2.5, main.get_strength([1, 1, 4, 4, 5]))
        self.assertEqual(3, main.get_strength([4, 1, 4, 4, 5]))
        self.assertEqual(3.5, main.get_strength([4, 5, 4, 4, 5]))
        self.assertEqual(4, main.get_strength([4, 5, 4, 4, 4]))
        self.assertEqual(5, main.get_strength([6, 6, 6, 6, 6]))

        # With Joker
        self.assertEqual(2, main.get_strength([1, 2, 0, 4, 5]))
        self.assertEqual(3, main.get_strength([1, 1, 0, 4, 5]))
        self.assertEqual(3, main.get_strength([1, 0, 0, 4, 5]))
        self.assertEqual(4, main.get_strength([1, 0, 0, 4, 4]))
        self.assertEqual(4, main.get_strength([4, 1, 4, 4, 0]))
        self.assertEqual(4, main.get_strength([4, 5, 4, 0, 0]))
        self.assertEqual(3.5, main.get_strength([4, 5, 4, 0, 5]))
        self.assertEqual(5, main.get_strength([0, 0, 0, 0, 6]))
        self.assertEqual(5, main.get_strength([0, 0, 0, 0, 0]))

    # def test_input_example_1(self):
    #     data = main.read_file("inputs/example1.txt")
    #     cards = main.parse_cards(data)
    #     self.assertEqual(6440, main.solve_part1(cards))
    #
    # def test_input_example_2(self):
    #     data = main.read_file("inputs/example2.txt")
    #     self.assertEqual(0, main.solve_part2(data))


if __name__ == '__main__':
    unittest.main()
