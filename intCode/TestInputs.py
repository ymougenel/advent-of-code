import unittest
import intCode


class TestInputs(unittest.TestCase):

    def setUp(self):
        pass

    def test_day2_example_part1(self):
        data = intCode.read_file("inputs/day2_example.input")
        res = intCode.run_simulation(data)
        self.assertEqual(res[0], 3500)

    def test_day2_input_part1(self):
        data = intCode.read_file("inputs/day2.input")
        intCode.restore_alarm(data, 12, 2)
        res = intCode.run_simulation(data)
        self.assertEqual(res[0], 3267740)

    def test_day2_input_part2(self):
        data = intCode.read_file("inputs/day2.input")
        res = intCode.found_matching_noun_verb(data)
        self.assertEqual(res, 7870)


if __name__ == '__main__':
    unittest.main()
