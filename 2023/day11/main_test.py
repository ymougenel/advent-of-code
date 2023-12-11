import unittest
import main


class main_test(unittest.TestCase):

    def test_space(self):
        data = main.read_file("inputs/example1.txt")
        main.detect_empy_rows(data)
        self.assertEqual([3, 7], main.empty_rows)
        main.detect_empy_cols(data)
        self.assertEqual([2, 5, 8], main.empty_cols)

    def test_distance(self):
        data = main.read_file("inputs/example1.txt")
        main.detect_empy_rows(data)
        main.detect_empy_cols(data)
        main.detect_stars(data)
        self.assertEqual(15, main.calculate_distance(main.stars[0], main.stars[6], 2))
        self.assertEqual(17, main.calculate_distance(main.stars[2], main.stars[5], 2))
        self.assertEqual(5, main.calculate_distance(main.stars[7], main.stars[8], 2))


if __name__ == '__main__':
    unittest.main()
