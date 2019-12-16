import unittest
import intCode


class TestIntcode(unittest.TestCase):


    # Test Addition
    def test_instruction1(self):
        # Single digit instruction
        data = [1, 0, 0, 0, 99]
        intCode.process_instruction(0, data)
        self.assertEqual(data, [2, 0, 0, 0, 99])

        # Triple digit instruction
        data = [102, 4, 3, 4, 33]
        intCode.process_instruction(0, data)
        self.assertEqual(data, [102, 4, 3, 4, 16])

        # Full digit instruction
        data = [1002, 4, 3, 4, 33]
        intCode.process_instruction(0, data)
        self.assertEqual(data, [1002, 4, 3, 4, 99])

    # Test multiplication
    def test_instruction2(self):
        # Single digit instruction
        data = [2, 3, 0, 3, 99]
        intCode.process_instruction(0, data)
        self.assertEqual(data, [2, 3, 0, 6, 99])

        # Triple digit instruction
        data = [102, 3, 0, 3, 99]
        intCode.process_instruction(0, data)
        self.assertEqual(data, [102, 3, 0, 306, 99])

        # Full digit instruction
        data = [1002, 3, 0, 3, 99]
        intCode.process_instruction(0, data)
        self.assertEqual(data, [1002, 3, 0, 0, 99])

    # Test input
    def test_instruction3(self):
        data = [3, 2, 3, 99]
        intCode.process_instruction(0, data, 42)
        self.assertEqual(data, [3, 2, 42, 99])

    # Test jump if
    def test_instruction5(self):
        # Single digit instruction
        data = [5, 3, 4, 1, 0]
        res = intCode.process_instruction(0, data)
        self.assertEqual(res[1], 0)
        data = [5, 3, 4, 0, 5]
        res = intCode.process_instruction(0, data)
        self.assertEqual(res[1], 0)

        # Triple digit instruction
        data = [105, 1, 3, 4, 5]
        res = intCode.process_instruction(0, data)
        self.assertEqual(res[1], 4  )
        data = [105, 0, 3, 4, 5]
        res = intCode.process_instruction(0, data)
        self.assertEqual(res[1], 0)

    # Test lesser than
    def test_instruction7(self):
        # Single digit instruction
        data = [7, 2, 3, 4, 42]
        intCode.process_instruction(0, data)
        self.assertEqual(data, [7, 2, 3, 4, 1])
        data = [7, 4, 3, 4, 42]
        intCode.process_instruction(0, data)
        self.assertEqual(data, [7, 4, 3, 4, 0])

        # Triple digit instruction
        data = [107, 2, 3, 4, 42]
        intCode.process_instruction(0, data)
        self.assertEqual(data, [107, 2, 3, 4, 1])
        data = [107, 5, 3, 4, 1]
        intCode.process_instruction(0, data)
        self.assertEqual(data, [107, 5, 3, 4, 0])

        # Full digit instruction
        data = [1107, 3, 4, 4, 99]
        intCode.process_instruction(0, data)
        self.assertEqual(data, [1107, 3, 4, 4, 1])
        data = [1107, 4, 3, 4, 42]
        intCode.process_instruction(0, data)
        self.assertEqual(data, [1107, 4, 3, 4, 0])

    def test_instruction99(self):
        data = [99]
        intCode.process_instruction(0, data)
        self.assertEqual(data, [99])
if __name__ == '__main__':
    unittest.main()
