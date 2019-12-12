import unittest
import day3
import numpy as np

class TestDay3(unittest.TestCase):

    def setUp(self):
        self.SIZE = 1500
        self.panel = np.zeros((self.SIZE, self.SIZE), dtype=complex)
        self.central_port = (self.SIZE // 2, self.SIZE // 2)

    # def test_manhattan_distance(self):
    #     p1=(0,0)
    #     p2=(3,3)
    #     self.assertEqual('foo'.upper(), 'FOO')

    def test_example1(self):
        wires = day3.read_wires("wires_example1.txt")
        day3.displayPaths(self.panel, self.central_port, wires, self.SIZE)
        distance = day3.find_closest_intersection_distance(self.central_port, self.panel)
        self.assertEqual(distance, 6)

    def test_example2(self):
        wires = day3.read_wires("wires_example2.txt")
        day3.displayPaths(self.panel, self.central_port, wires, self.SIZE)
        distance = day3.find_closest_intersection_distance(self.central_port, self.panel)
        self.assertEqual(distance, 159)

    def test_example3(self):
        wires = day3.read_wires("wires_example3.txt")
        day3.displayPaths(self.panel, self.central_port, wires, self.SIZE)
        distance = day3.find_closest_intersection_distance(self.central_port, self.panel)
        self.assertEqual(distance, 135)


if __name__ == '__main__':
    unittest.main()
