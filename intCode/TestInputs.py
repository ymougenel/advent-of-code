import unittest
from intCode import IntCode


class TestInputs(unittest.TestCase):

    def setUp(self):
        self.intCode = IntCode()
    #
    # def test_day2_example_part1(self):
    #     self.intCode.init_numbers_from_file("inputs/day2_example.input")
    #     self.intCode.run_simulation()
    #     self.assertEqual(self.intCode.numbers[0], 3500)
    #
    # def test_day2_input_part1(self):
    #     self.intCode.init_numbers_from_file("inputs/day2.input")
    #     self.intCode.restore_alarm(12, 2)
    #     self.intCode.run_simulation()
    #     self.assertEqual(self.intCode.numbers[0], 3267740)
    #
    # def test_day5_part1(self):
    #     self.intCode.init_numbers_from_file("inputs/day5.input")
    #     self.intCode.input = 1
    #     self.intCode.run_simulation()
    #     self.assertEqual(self.intCode.outputs[-1], 13210611)

    def test_day5_part2(self):
        self.intCode.init_numbers_from_file("inputs/day5.input")
        self.intCode.input = 5
        self.intCode.run_simulation()
        self.assertEqual(self.intCode.outputs[0], 584126)
if __name__ == '__main__':
    unittest.main()
