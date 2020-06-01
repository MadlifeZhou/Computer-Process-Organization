import unittest
from parse_str import parse_str, calculate, BracketDismatchError


class TestParseStr(unittest.TestCase):

    
    def test_custom_parameter(self):
        str_1 = '6-3+y'
        self.assertEqual(calculate(number_list=parse_str(str_1), custom_function=None, custom_parameter={'y':1}), 4)
        self.assertEqual(calculate(number_list=parse_str(str_1), custom_function=None, custom_parameter={'y':2}), 5)

    def test_custom_function(self):
        str_1 = 'f(x)+1.1'
        self.assertEqual(calculate(number_list=parse_str(str_1), custom_function=lambda x: x+1, custom_parameter={'x':1.1}), 3.2)
        self.assertEqual(calculate(number_list=parse_str(str_1), custom_function=lambda x: x+1, custom_parameter={'x':2}), 4.1)

    def test_custom_function_and_parameter(self):
        str_1 = 'f(x)+y+z*3'
        self.assertEqual(calculate(number_list=parse_str(str_1), custom_function=lambda x: x+1, 
                                   custom_parameter={'x':1, 'y':2, 'z':1}), 7)
        self.assertEqual(calculate(number_list=parse_str(str_1), custom_function=lambda x: x+1, 
                                   custom_parameter={'x':3, 'y':6, 'z':7}), 31)

    def test_add(self):
        self.assertEqual(calculate(number_list=parse_str('1+2')), 3)
        self.assertEqual(calculate(number_list=parse_str('5+6+1')), 12)
        self.assertEqual(calculate(number_list=parse_str('1.2+2.5')), 3.7)
        self.assertEqual(calculate(number_list=parse_str('1.2+2.5+2.2')), 5.9)

    def test_sub(self):
        self.assertEqual(calculate(number_list=parse_str('1-2')), -1)
        self.assertEqual(calculate(number_list=parse_str('1-2-4')), -5)
        self.assertEqual(calculate(number_list=parse_str('2.5-1.2')), 1.3)

    def test_mul(self):
        self.assertEqual(calculate(number_list=parse_str('3*1')), 3)
        self.assertEqual(calculate(number_list=parse_str('2*3*4')), 24)

    def test_div(self):
        self.assertEqual(calculate(number_list=parse_str('3/1')), 3.0)

    def test_negative_tests(self):
        str_1 = '3/0'
        str_2 = '1+2)'
        self.assertRaises(ZeroDivisionError, calculate(number_list=parse_str(str_1)))
        self.assertRaises(BracketDismatchError, parse_str(str_2))
        

    def test_mixed_str(self):
        str_1 = '(4-1)*(pow(2, 3)+sin(0))-f(x)'
        str_2 = '3*(pow(2, 3)+cos(0))-f(x)'
        str_3 = '1+f(x)'
        str_4 = '1+f(x,y)+z'
        self.assertEqual(calculate(number_list=parse_str(str_1), custom_function=lambda x: x + 1, custom_parameter={'x': 1}), 22)
        self.assertEqual(calculate(number_list=parse_str(str_2), custom_function=lambda x: x * 1, custom_parameter={'x': 1}), 26)
        self.assertEqual(calculate(number_list=parse_str(str_3), custom_function=lambda x: x ** 2, custom_parameter={'x': 1}), 2)
        self.assertEqual(calculate(number_list=parse_str(str_4), custom_function=lambda x, y:x*y, custom_parameter={'x': 2, 'y': 5, 'z': 8}), 19)

    def test_graph(self):
        str_1 = '(4-1)*(pow(2,3)+cos(0))-f(x)'
        graph_2 = """digraph G {
  INPUT[shape=rect label="(4-1)*(pow(2,3)+cos(0))-f(x)"];
  OUTPUT[shape=rect];
  node_0[label="4"];
  INPUT -> node_0;
  node_1[label="1"];
  INPUT -> node_1;
  node_2[label="-" shape=square];
  node_3[label="pow(2,3)"];
  INPUT -> node_3;
  node_4[label="cos(0)"];
  INPUT -> node_4;
  node_5[label="+" shape=square];
  node_6[label="*" shape=square];
  node_7[label="f(x)"];
  INPUT -> node_7;
  node_8[label="-" shape=square];
  node_result_of_pow[label="8"];
  node_3 -> node_result_of_pow;
  node_result_of_cos[label="1"];
  node_4 -> node_result_of_cos;
  node_result_of_f[label="2"];
  node_7 -> node_result_of_f;
  node_1 -> node_2;
  node_0 -> node_2;
  node_result_of_cos -> node_5;
  node_result_of_pow -> node_5;
  node_5 -> node_6;
  node_2 -> node_6;
  node_6 -> node_8;
  node_result_of_f -> node_8;
  node_8 -> OUTPUT[label="="];
}"""
        graph = calculate(number_list=parse_str(str_1), str_expression=str_1,
                                      custom_function=lambda x: x+1, custom_parameter={'x':1})
        self.assertEqual(graph, graph_2)



if __name__ == '__main__':
    unittest.main()

    