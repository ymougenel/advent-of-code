import unittest
import main

class main_test(unittest.TestCase):

    def test_extension(self):
        initial_map = main.read_file("inputs/part1.example")
        extended_map = main.read_file("inputs/part2.example")
        self.assertEqual(extended_map, main.extend_map(initial_map))

    def test_input_exemple(self):
        map = main.read_file("inputs/part1.example")
        map = extend_map(map, 1)
        infos = init_infos(map)
        solve(map, infos)
        self.assertEqual(40, infos[(len(map) - 1, len(map[0]) - 1)])

if __name__ == '__main__':
    unittest.main()
