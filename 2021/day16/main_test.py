import unittest
import main

hexa_example1 = "D2FE28"
bin_example1 = "110100101111111000101000"
hexa_example2 = "38006F45291200"
bin_example2 = "00111000000000000110111101000101001010010001001000000000"
hexa_example3 = "EE00D40C823060"
bin_example3 = "11101110000000001101010000001100100000100011000001100000"
class main_test(unittest.TestCase):

    def test_conversion(self):
        self.assertEqual(bin_example1, main.transform_hexa_to_binary(hexa_example1))
        self.assertEqual(bin_example2, main.transform_hexa_to_binary(hexa_example2))

    def test_get_version(self):
        self.assertEqual(6, main.parse_to_array(bin_example1)[1])
        self.assertEqual(1, main.parse_to_array(bin_example2)[1])
        self.assertEqual(7, main.parse_to_array(bin_example3)[1])

        bin = main.transform_hexa_to_binary("8A004A801A8002F478")
        self.assertEqual(4, main.parse_to_array(bin)[1])
if __name__ == '__main__':
    unittest.main()
