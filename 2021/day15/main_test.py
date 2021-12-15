import unittest
import main
import numpy as np

vec_A = np.array([1, 0, 0])
vec_B = np.array([0, 1, 0])
vec_C = np.array([0, 0, 1])
transfo_M1 = np.array([
    [0, 3, 0],
    [0, 0, 2],
    [2, 0, 0]
])


class main_test(unittest.TestCase):
    # def test_input_exemple_1(self):
    #     data = main.read_file("inputs/part1.example")
    #     self.assertEqual(0, 1)
    #
    # def test_input_exemple_2(self):
    #     data = main.read_file_sliding_window("inputs/part2.example")
    #     self.assertEqual(0, 0)

    def test_map_letter_to_vector(self):
        # self.assertEqual(vec_A, 0)
        np.testing.assert_equal(vec_A, main.map_letter_to_vector("A", 3))
        np.testing.assert_equal(vec_B, main.map_letter_to_vector("B", 3))
        np.testing.assert_equal(vec_C, main.map_letter_to_vector("C", 3))

    def test_get_transformation_matrix(self):
        data = main.read_file("inputs/my_example")
        res = main.get_transformation_matrix(data[2:], 3)
        np.testing.assert_equal(transfo_M1, main.get_transformation_matrix(data[2:], 3))

    def test_transform(self):
        np.testing.assert_equal(vec_C, main.transform(vec_A, vec_B, transfo_M1, 3))
        np.testing.assert_equal(vec_B, main.transform(vec_C, vec_A, transfo_M1, 3))
        np.testing.assert_equal(vec_B, main.transform(vec_B, vec_C, transfo_M1, 3))
        np.testing.assert_equal(np.zeros(3, int), main.transform(vec_A, vec_C, transfo_M1, 3))


if __name__ == '__main__':
    unittest.main()
