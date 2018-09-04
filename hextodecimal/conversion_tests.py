import unittest
import hex_to_decimal

class HexToDecimalConversionTest(unittest.TestCase):
    """Tests for the hex_to_decimal.convert() function"""

    def test_1(self):
        """should return 175 when the input is 'AF'"""
        self.assertEqual(hex_to_decimal.convert('AF'), 175)

    def test_2(self):
        """should return 2765 when the input is 'ACD'"""
        self.assertEqual(hex_to_decimal.convert('ACD'), 2765)

    def test_3(self):
        """should return 2738 when the input is 'AB2'"""
        self.assertEqual(hex_to_decimal.convert('AB2'), 2738)

    def test_4(self):
        """should return 255 when the input is 'FF'"""
        self.assertEqual(hex_to_decimal.convert('FF'), 255)

if __name__ == '__main__':
    unittest.main()