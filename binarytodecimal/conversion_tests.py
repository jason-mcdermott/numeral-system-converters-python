import unittest
import binary_to_decimal

class BinaryToDecimalConversionTest(unittest.TestCase):
    """Tests for the binary_to_decimal.convert() function"""

    def test_1(self):
        """should return 4 when the input is '0100'"""
        self.assertEqual(binary_to_decimal.convert('0100'), 4)

    def test_2(self):
        """should return 122 when the input is '01111010'"""
        self.assertEqual(binary_to_decimal.convert('01111010'), 122)

    def test_3(self):
        """should return 255 when the input is '000011111111'"""
        self.assertEqual(binary_to_decimal.convert('000011111111'), 255)

    def test_4(self):
        """should return 4096 when the input is '0001000000000000'"""
        self.assertEqual(binary_to_decimal.convert('0001000000000000'), 4096)

if __name__ == '__main__':
    unittest.main()