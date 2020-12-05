import unittest
import day5


class day4_test(unittest.TestCase):


    def test_range_splitting(self):
        # F=Lower Half
        self.assertEqual(day5.split_range((0, 127), "F"), (0, 63))
        self.assertEqual(day5.split_range((0, 63), "F"), (0, 31))
        self.assertEqual(day5.split_range((0, 31), "F"), (0, 15))
        self.assertEqual(day5.split_range((32, 63), "F"), (32, 47))
        self.assertEqual(day5.split_range((44, 47), "F"), (44, 45))
        self.assertEqual(day5.split_range((44, 45), "F"), (44, 44))

        # B=UpperHalf
        self.assertEqual(day5.split_range((0, 127), "B"), (64, 127))
        self.assertEqual(day5.split_range((64, 127), "B"), (96, 127))
        self.assertEqual(day5.split_range((96, 127), "B"), (112, 127))
        self.assertEqual(day5.split_range((0, 63), "B"), (32, 63))
        self.assertEqual(day5.split_range((32, 47), "B"), (40, 47))
        self.assertEqual(day5.split_range((40, 47), "B"), (44, 47))


    def test_process_passport_translation(self):
        self.assertEqual(day5.process_passport_translation("FBFBBFFRLR"), (44, 5))


    def test_process_passport(self):
        self.assertEqual(day5.process_passport("BFFFBBFRRR"), 567)
        self.assertEqual(day5.process_passport("FFFBBBFRRR"), 119)
        self.assertEqual(day5.process_passport("BBFFBBFRLL"), 820)
        self.assertEqual(day5.process_passport("FBFBBFFRLR"), 357)


if __name__ == '__main__':
    unittest.main()
