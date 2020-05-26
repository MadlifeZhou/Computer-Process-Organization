import unittest
from parse_str import parse_str, calculate


class TestParseStr(unittest.TestCase):

    
    def test_custom_parameter(self):
        str_1 = '6-3+y'
        self.assertEqual(calculate(number_list=parse_str(str_1), custom_function=None, custom_parameter={'y':1}), 4)
        self.assertEqual(calculate(number_list=parse_str(str_1), custom_function=None, custom_parameter={'y':2}), 5)

    def test_custom_function(self):
        str_1 = 'f(x)+1'
        self.assertEqual(calculate(number_list=parse_str(str_1), custom_function=lambda x: x+1, custom_parameter={'x':1}), 3)
        self.assertEqual(calculate(number_list=parse_str(str_1), custom_function=lambda x: x+1, custom_parameter={'x':2}), 4)

    def test_custom_function_and_parameter(self):
        str_1 = 'f(x)+y+z*3'
        self.assertEqual(calculate(number_list=parse_str(str_1), custom_function=lambda x: x+1, 
                                   custom_parameter={'x':1, 'y':2, 'z':1}), 7)
        self.assertEqual(calculate(number_list=parse_str(str_1), custom_function=lambda x: x+1, 
                                   custom_parameter={'x':3, 'y':6, 'z':7}), 31)

    def test_add(self):
        self.assertEqual(calculate(number_list=parse_str('1+2')), 3)
        self.assertEqual(calculate(number_list=parse_str('5+6+1')), 12)

    def test_sub(self):
        self.assertEqual(calculate(number_list=parse_str('1-2')), -1)
        self.assertEqual(calculate(number_list=parse_str('1-2-4')), -5)

    def test_mul(self):
        self.assertEqual(calculate(number_list=parse_str('3*1')), 3)
        self.assertEqual(calculate(number_list=parse_str('2*3*4')), 24)

    def test_div(self):
        self.assertEqual(calculate(number_list=parse_str("3/1")), 3.0)
        

    def test_mixed_str(self):
        str_1 = '(4-1)*(pow(2, 3)+sin0)-f(x)'
        str_2 = '3*(pow(2, 3)+cos0)-f(x)'
        str_3 = '1+f(x)'
        self.assertEqual(calculate(number_list=parse_str(str_1), custom_function=lambda x: x + 1, custom_parameter={'x': 1}), 22)
        self.assertEqual(calculate(number_list=parse_str(str_2), custom_function=lambda x: x * 1, custom_parameter={'x': 1}), 26)
        self.assertEqual(calculate(number_list=parse_str(str_3), custom_function=lambda x: x ** 2, custom_parameter={'x': 1}), 2)
    