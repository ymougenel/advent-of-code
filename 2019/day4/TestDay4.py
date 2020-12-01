import unittest
import day4

class TestDay4(unittest.TestCase):

    def setUp(self):
        pass

    def test_two_adjacent_digits(self):
        self.assertTrue(day4.check_two_adjacent_digits(111111))
        self.assertTrue(day4.check_two_adjacent_digits(223450))
        self.assertTrue(day4.check_two_adjacent_digits(123455))
        self.assertFalse(day4.check_two_adjacent_digits(123456))

    def test_never_decrease(self):
        self.assertFalse(day4.check_never_decrease(223450))
        self.assertTrue(day4.check_never_decrease(111111))
        self.assertTrue(day4.check_never_decrease(123456))


    def test_adjacents_not_part_larger_group(self):
        self.assertFalse(day4.check_adjacents_not_part_larger_group(222450))
        self.assertTrue(day4.check_adjacents_not_part_larger_group(111144))
        self.assertTrue(day4.check_adjacents_not_part_larger_group(123356))

if __name__ == '__main__':
    unittest.main()
