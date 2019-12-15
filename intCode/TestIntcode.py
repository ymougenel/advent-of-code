import unittest
import intCode


class TestIntcode(unittest.TestCase):

    def setUp(self):
        pass

    def test_instruction1(self):
       # Single digit instruction
        data = ["1", "0", "0", "0", "99"]
        intCode.process_instruction(0, data)
        self.assertEqual(data, ["2", "0", "0", "0", "99"])

        # Double digit instruction
        data = ["02", "4", "3", "4", "33"]
        intCode.process_instruction(0, data)
        self.assertEqual(data, ["02", "4", "3", "4", "132"])

        # Triple digit instruction
        data = ["102", "4", "3", "4", "33"]
        intCode.process_instruction(0, data)
        self.assertEqual(data, ["102", "4", "3", "4", "16"])

        # Full digit instruction
        data = ["1002", "4", "3", "4", "33"]
        intCode.process_instruction(0, data)
        self.assertEqual(data, ["1002", "4", "3", "4", "99"])

    def test_instruction2(self):
        # Single digit instruction
        data = ["2", "3", "0", "3", "99"]
        intCode.process_instruction(0, data)
        self.assertEqual(data, ["2", "3", "0", "6", "99"])

        # Double digit instruction
        data = ["02", "3", "0", "3", "99"]
        intCode.process_instruction(0, data)
        self.assertEqual(data, ["02", "3", "0", "6", "99"])

        # Triple digit instruction
        data = ["102", "3", "0", "3", "99"]
        intCode.process_instruction(0, data)
        self.assertEqual(data, ["102", "3", "0", "306", "99"])

        # Full digit instruction
        data = ["1002", "3", "0", "3", "99"]
        intCode.process_instruction(0, data)
        self.assertEqual(data, ["1002", "3", "0", "0", "99"])

    def test_instruction3(self):
        data = ["3", "2", "3", "99"]
        intCode.process_instruction(0, data, 42)
        self.assertEqual(data, ["3", "2", "42", "99"])

    def test_instruction99(self):
        data = ["99"]
        intCode.process_instruction(0, data)
        self.assertEqual(data, ["99"])

if __name__ == '__main__':
    unittest.main()
