import unittest
from intCode import IntCode


class TestIntCode(unittest.TestCase):

    def setUp(self):
        self.intCode = IntCode()

    # Test Addition
    def test_instruction1(self):
        # Single digit instruction
        data = [1, 0, 0, 0, 99]
        self.intCode.numbers = data
        self.intCode.process_instruction()
        self.assertEqual(data, [2, 0, 0, 0, 99])

        # Triple digit instruction
        data = [101, 4, 3, 4, 33]
        self.intCode.numbers = data
        self.intCode.process_instruction()
        self.assertEqual(data, [101, 4, 3, 4, 8])

        # Full digit instruction
        data = [1001, 4, 3, 4, 33]
        self.intCode.numbers = data
        self.intCode.process_instruction()
        self.assertEqual(data, [1001, 4, 3, 4, 36])

        # With relative base
        data = [1001, 4, 3, 4, 33]  # Nothing change
        self.intCode.numbers = data
        self.intCode.relative_base = 2
        self.intCode.process_instruction()
        self.assertEqual(data, [1001, 4, 3, 4, 36])

        data = [1201, -2, 4, 4, 33]
        self.intCode.numbers = data
        self.intCode.relative_base = 2
        self.intCode.process_instruction()
        self.assertEqual(data, [1201, -2, 4, 4, 1205])

    # Test multiplication
    def test_instruction2(self):
        # Single digit instruction
        data = [2, 3, 0, 3, 99]
        self.intCode.numbers = data
        self.intCode.process_instruction()
        self.assertEqual(data, [2, 3, 0, 6, 99])

        # Triple digit instruction
        data = [102, 3, 0, 3, 99]
        self.intCode.numbers = data
        self.intCode.process_instruction()
        self.assertEqual(data, [102, 3, 0, 306, 99])

        # Full digit instruction
        data = [1002, 3, 0, 3, 99]
        self.intCode.numbers = data
        self.intCode.process_instruction()
        self.assertEqual(data, [1002, 3, 0, 0, 99])

    # Test input
    def test_instruction3(self):
        data = [3, 2, 3, 99]
        self.intCode.numbers = data
        self.intCode.input = 42
        self.intCode.process_instruction()
        self.assertEqual(data, [3, 2, 42, 99])

    # Test jump if
    def test_instruction5(self):
        # Single digit instruction
        data = [5, 3, 4, 1, 0]
        self.intCode.numbers = data
        self.intCode.process_instruction()
        self.assertEqual(self.intCode.cursor, 4)

        data = [5, 3, 4, 0, 5]
        self.intCode.cursor = 0
        self.intCode.numbers = data
        self.intCode.process_instruction()
        self.assertEqual(self.intCode.cursor, 0)

        # Triple digit instruction
        data = [105, 1, 3, 4, 5]
        self.intCode.cursor = 0
        self.intCode.numbers = data
        self.intCode.process_instruction()
        self.assertEqual(self.intCode.cursor, 3)

        data = [105, 0, 3, 4, 5]
        self.intCode.cursor = 0
        self.intCode.numbers = data
        self.intCode.process_instruction()
        self.assertEqual(self.intCode.cursor, 0)

    # Test lesser than
    def test_instruction7(self):
        # Single digit instruction
        data = [7, 2, 3, 4, 42]
        self.intCode.numbers = data
        self.intCode.process_instruction()
        self.assertEqual(data, [7, 2, 3, 4, 1])
        data = [7, 4, 3, 4, 42]
        self.intCode.numbers = data
        self.intCode.process_instruction()
        self.assertEqual(data, [7, 4, 3, 4, 0])

        # Triple digit instruction
        data = [107, 2, 3, 4, 42]
        self.intCode.numbers = data
        self.intCode.process_instruction()
        self.assertEqual(data, [107, 2, 3, 4, 1])
        data = [107, 5, 3, 4, 1]
        self.intCode.numbers = data
        self.intCode.process_instruction()
        self.assertEqual(data, [107, 5, 3, 4, 0])

        # Full digit instruction
        data = [1107, 3, 4, 4, 99]
        self.intCode.numbers = data
        self.intCode.process_instruction()
        self.assertEqual(data, [1107, 3, 4, 4, 1])
        data = [1107, 4, 3, 4, 42]
        self.intCode.numbers = data
        self.intCode.process_instruction()
        self.assertEqual(data, [1107, 4, 3, 4, 0])

    # Test update relative base
    def test_instruction9(self):
        data = [109, 19]
        self.intCode.numbers = data
        self.intCode.relative_base = 2000
        self.intCode.process_instruction()
        self.assertEqual(self.intCode.relative_base, 2019)

    def test_instruction99(self):
        data = [99]
        self.intCode.numbers = data
        self.intCode.process_instruction()
        self.assertEqual(data, [99])


if __name__ == '__main__':
    unittest.main()
