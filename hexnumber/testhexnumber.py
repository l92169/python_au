import unittest
from hexnumber.hexnum import Node, HexNumber, Solution
class TestHexNumber(unittest.TestCase):
    def test_num(self):
        num = str(HexNumber(""))
        self.assertEqual(num,"")

        num = str(HexNumber("1563"))
        self.assertEqual(num, "1563")

        num = str(HexNumber("A"))
        self.assertEqual(num, "A")

class TestSolution(unittest.TestCase):
    def test_from_hex_to_decimal(self):
        test = Solution(HexNumber(''), HexNumber(''))
        self.assertEqual(test.from_hex_to_decimal('1'), 1)
        self.assertEqual(test.from_hex_to_decimal('A'), 10)
        self.assertEqual(test.from_hex_to_decimal('F'), 15)


    def test_from_decimal_to_hex(self):
        test = Solution(HexNumber(''), HexNumber(''))
        self.assertEqual(test.from_decimal_to_hex(1), '1')
        self.assertEqual(test.from_decimal_to_hex(10), 'A')
        self.assertEqual(test.from_decimal_to_hex(15), 'F')

    def test_add(self):
        test = Solution(HexNumber('8'), HexNumber('0'))
        test.add()
        self.assertEqual(str(test.res),'8')

        test = Solution(HexNumber('A'), HexNumber('A'))
        test.add()
        self.assertEqual(str(test.res), '14')

        test = Solution(HexNumber('F5'), HexNumber('F6'))
        test.add()
        self.assertEqual(str(test.res), '1EB')
