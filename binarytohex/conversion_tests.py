import unittest
import binary_to_hex

class BinaryToHexConversionTest(unittest.TestCase):
    """Tests for the binary_to_hex.convert() function"""

    def test_1(self):
        """should return '475' when the input is '010001110101'"""
        self.assertEqual(binary_to_hex.convert('010001110101'), '475')

    def test_2(self):
        """should return 'FA5A' when the input is '1111101001011010'"""
        self.assertEqual(binary_to_hex.convert('1111101001011010'), 'FA5A')

    def test_3(self):
        """should return '0FF2F' when the input is '00001111111100101111'"""
        self.assertEqual(binary_to_hex.convert('00001111111100101111'), '0FF2F')

    def test_4(self):
        """should return 'C8009' when the input is '11001000000000001001'"""
        self.assertEqual(binary_to_hex.convert('11001000000000001001'), 'C8009')

if __name__ == '__main__':
    unittest.main()