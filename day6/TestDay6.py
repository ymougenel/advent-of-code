import unittest
import day6


class TestDay6(unittest.TestCase):

    def setUp(self):
        # COM - A - B
        self.g1 = {'COM': ['A'], 'A': ['B']}
        #     D
        #    /
        # COM - A - B
        self.g2 = {'COM': ['A', 'D'], 'A': ['B']}
        #         G - H
        #        /
        # COM - B - C - D - E
        #                \
        #                 I
        self.g3 = {'COM': ['B'], 'B': ['C', 'G'], 'C': ['D'], 'D': ['E', 'I'], 'G': ['H']}
        #         G - H       J - K - L
        #        /           /
        # COM - B - C - D - E - F
        #                \
        #                 I
        self.g4 = {'COM': ['B'], 'B': ['C', 'G'], 'C': ['D'], 'D': ['E', 'I'], 'E': ['F', 'J'], 'G': ['H'], 'J': ['K'], 'K': ['L']}



    # Test direct orbits
    def test_count_direct_orbits(self):
        self.assertEqual(day6.count_direct_orbits(self.g1,), 2)
        self.assertEqual(day6.count_direct_orbits(self.g2,), 3)
        self.assertEqual(day6.count_direct_orbits(self.g3,), 7)
        self.assertEqual(day6.count_direct_orbits(self.g4,), 11)

    # Test indirect orbits
    def test_count_indirects_orbits(self):
        self.assertEqual(day6.count_indirect_orbits(self.g1,), 1)
        self.assertEqual(day6.count_indirect_orbits(self.g2,), 1)
        self.assertEqual(day6.count_indirect_orbits(self.g3,), 12)
        self.assertEqual(day6.count_indirect_orbits(self.g4,), 31)


if __name__ == '__main__':
    unittest.main()
