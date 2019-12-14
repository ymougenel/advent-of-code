import unittest
import intCode


class TestIntcode(unittest.TestCase):

    def setUp(self):
        pass

    def test_instruction1(self):
        data = [1, 0, 0, 0, 99]
        intCode.instruction1(0, data)
        self.assertEqual(data, [2, 0, 0, 0, 99])

    def test_instruction2(self):
        data = [2, 3, 0, 3, 99]
        intCode.instruction2(0, data)
        self.assertEqual(data, [2, 3, 0, 6, 99])

    def test_instruction2(self):
        data = [2, 3, 0, 3, 99]
        intCode.instruction2(0, data)
        self.assertEqual(data, [2, 3, 0, 6, 99])

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
