import unittest
from parse_str import parse_str, calculate
class TestParseStr(unittest.TestCase):
    def test_parse_str(self):
        str_1 = '1+2'
        str_2 = '3*(2+6)'
        str_3 = '(4-1)*(pow(2, 3)+sin0)-f(x)'
        str_4 = '3*(pow(2, 3)+cos0)-f(x)'
        str_5 = '1+f(x)'
        self.assertEqual(calculate(parse_str(str_1)), '3')
        self.assertEqual(calculate(parse_str(str_2)), '24')
        self.assertEqual(calculate(parse_str(str_3), lambda x:x+1, 1), '22')
        self.assertEqual(calculate(parse_str(str_4), lambda x:x*1, 1), '26')
        self.assertEqual(calculate(parse_str(str_5), lambda x:x**2, 2), '5')