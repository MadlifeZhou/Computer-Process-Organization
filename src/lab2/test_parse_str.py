import unittest
from parse_str import parse_str, calculate


class TestParseStr(unittest.TestCase):
    def test_Add(self):
        self.assertEqual(calculate(parse_str("1+2")), "3")
        self.assertEqual(calculate(parse_str("5+6")), "11")
        self.assertEqual(calculate(parse_str("2+2+5+7")), "16")
        self.assertEqual(calculate(parse_str("8+5+0+2+6")), "21")

    def test_sub(self):
        self.assertEqual(calculate(parse_str("1-2")), "-1")
        self.assertEqual(calculate(parse_str("1-6-7")), "-12")
        self.assertEqual(calculate(parse_str("4-8-7-4")), "-15")
        self.assertEqual(calculate(parse_str("7-9-8-5-2")), "-17")

    def test_mul(self):
        self.assertEqual(calculate(parse_str("3*1")), "3")
        self.assertEqual(calculate(parse_str("2*3*4")), "24")
        self.assertEqual(calculate(parse_str("5*3*6*9")), "810")
        self.assertEqual(calculate(parse_str("4*3*7*9*2")), "1512")

    def test_div(self):
        self.assertEqual(calculate(parse_str("3/1")), "3.0")
        self.assertEqual(calculate(parse_str("3/2")), "1.5")
        self.assertEqual(calculate(parse_str("6/2")), "3.0")

    def test_mixed_str(self):
        str_1 = '(4-1)*(pow(2, 3)+sin0)-f(x)'
        str_2 = '3*(pow(2, 3)+cos0)-f(x)'
        str_3 = '1+f(x)'
        self.assertEqual(calculate(parse_str(str_1), lambda x: x + 1, 1), '22')
        self.assertEqual(calculate(parse_str(str_2), lambda x: x * 1, 1), '26')
        self.assertEqual(calculate(parse_str(str_3), lambda x: x ** 2, 2), '5')
