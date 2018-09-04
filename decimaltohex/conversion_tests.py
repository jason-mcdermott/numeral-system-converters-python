import unittest
import decimal_to_hex

class DecimalToHexConversionTest(unittest.TestCase):
    """Tests for the decimal_to_hex.convert() function"""

    def test_1(self):
        """should return '4' when the input is 4"""
        self.assertEqual(decimal_to_hex.convert(4), '4')

    def test_2(self):
        """should return '1DF' when the input is 479"""
        self.assertEqual(decimal_to_hex.convert(479), '1DF')

    def test_3(self):
        """should return '37E' when the input is 894"""
        self.assertEqual(decimal_to_hex.convert(894), '37E')

    def test_4(self):
        """should return 'CD4' when the input is 3284"""
        self.assertEqual(decimal_to_hex.convert(3284), 'CD4')

if __name__ == '__main__':
    unittest.main()