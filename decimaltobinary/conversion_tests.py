import unittest
import decimal_to_binary

class DecimalToBinaryConversionTest(unittest.TestCase):
    """Tests for the decimal_to_binary.convert() function"""

    def test_1(self):
        """should return '0100' when the input is 4"""
        self.assertEqual(decimal_to_binary.convert(4), '0100')

    def test_2(self):
        """should return '01111010' when the input is 122"""
        self.assertEqual(decimal_to_binary.convert(122), '01111010')

    def test_3(self):
        """should return '000011111111' when the input is 255"""
        self.assertEqual(decimal_to_binary.convert(255), '000011111111')

    def test_4(self):
        """should return '0001000000000000' when the input is 4096"""
        self.assertEqual(decimal_to_binary.convert(4096), '0001000000000000')

if __name__ == '__main__':
    unittest.main()