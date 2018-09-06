import unittest
import hex_to_binary

class HexToBinaryConversionTest(unittest.TestCase):
    """Tests for the hex_to_binary.convert() function"""

    def test_1(self):
        """should return '0011101010110010' when the input is '3AB2'"""
        self.assertEqual(hex_to_binary.convert('3AB2'), '0011101010110010')

    def test_2(self):
        """should return '0001111110011011' when the input is '1F9B'"""
        self.assertEqual(hex_to_binary.convert('1F9B'), '0001111110011011')

    def test_3(self):
        """should return '0101011011011111' when the input is '56DF'"""
        self.assertEqual(hex_to_binary.convert('56DF'), '0101011011011111')

    def test_4(self):
        """should return '1111101010111111' when the input is 'FABF'"""
        self.assertEqual(hex_to_binary.convert('FABF'), '1111101010111111')

if __name__ == '__main__':
    unittest.main()
