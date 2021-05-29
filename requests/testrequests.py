import unittest
from requests.requestss import *

class TestVerifier(unittest.TestCase):
    def test_check_prefixes(self):
         new = 'HEXNUMBER-1022 Added verifier'
         result = check_prefixes(new)
         expect = '('', True)'
         self.assertEqual(expect, result)

if __name__ == '__main__':
    unittest.main()