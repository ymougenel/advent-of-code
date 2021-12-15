import unittest
import main

class main_test(unittest.TestCase):

    def test_extension(self):
        initial_map = main.read_file("inputs/part1.example")
        extended_map = main.read_file("inputs/part2.example")
        self.assertEqual(extended_map, main.extend_map(initial_map))

    def test_input_exemple_2(self):
        self.assertEqual(0, 0)

if __name__ == '__main__':
    unittest.main()
