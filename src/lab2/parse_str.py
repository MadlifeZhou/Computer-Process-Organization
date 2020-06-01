from math import sin, cos, log

class MyStack(object):
    def __init__(self):
        self._lst = []

    def is_empty(self):
        return len(self._lst) == 0

    def push(self, element):
        self._lst.append(element)

    def pop(self):
        if self.is_empty():
            return
        else:
            return self._lst.pop()

    def top(self):
        if self.is_empty():
            return
        else:
            return self._lst[-1]

    def reverse(self):
        return self._lst.reverse()

def parse_str(expression):
    try:
        if not detection_of_bracket_matches(expression):
            raise BracketDismatchError(expression)
    except BracketDismatchError as e:
        print(e.msg)
        return
    
    number_stack, operator_stack, i = MyStack(), MyStack(), 0
    operator_priority = {'+': 1, '-': 1, '*': 2, '/': 2, '(': -1, ')': -1}
    while (i < len(expression)):
        tmp_str = ''
        # Elements like 'sin', 'cos', 'tan' will be considered as a number.
        if expression[i] not in operator_priority.keys() and 'a' <= expression[i] <= 'w':
            # 'f' means custom functions.
            if expression[i] == 'p' or expression[i] == 'f':
                while expression[i] not in list(operator_priority.keys())[0:4]:
                    tmp_str += expression[i]
                    i += 1
                    if i == len(expression): break
            else:
                while expression[i] not in list(operator_priority.keys())[0:4]:
                    tmp_str += expression[i]
                    if expression[i] == ')':
                        if i == len(expression): 
                            break
                        else:
                            i += 1
                            break
                    i += 1
                    #if i == len(expression) or expression[i] == ')': break
            if detection_of_bracket_matches(tmp_str): number_stack.push(tmp_str)
            else: 
                number_stack.push(tmp_str[0:(len(tmp_str)-1)])
                i -= 1
            if i == len(expression): break
        if expression[i].isdigit() or 'x' <= expression[i] <= 'z':
            # Digit will be pushed into stack directly.
            if i+1 < len(expression) and expression[i+1] == '.':
                tmp_float_num = expression[i] + expression[i+1]
                i += 2
                while expression[i].isdigit():
                    tmp_float_num += expression[i]
                    i += 1
                    if i >= len(expression): break
                number_stack.push(tmp_float_num)
            else:
                number_stack.push(expression[i])
                i += 1
        else:
            # Operator
            if operator_stack.is_empty() or expression[i] == '(':
                # Left bracket will be pushed into stack directly.
                operator_stack.push(expression[i])
                i += 1
            elif expression[i] != ')':
                # Priority of different operators.
                operator_priority_in_stack = operator_priority[operator_stack.top()]
                operator_priority_current = operator_priority[expression[i]]
                if operator_priority_in_stack >= operator_priority_current:
                    number_stack.push(operator_stack.pop())
                    operator_stack.push(expression[i])
                    i += 1
                else:
                    operator_stack.push(expression[i])
                    i += 1
            else:
                while (expression[i] == ')' and operator_stack.top() != '('):
                    # Right bracket.
                    number_stack.push(operator_stack.pop())
                if operator_stack.top() == '(':
                    operator_stack.pop()
                    i += 1
    while not operator_stack.is_empty():
        number_stack.push(operator_stack.pop())
    return number_stack._lst



def calculate(str_expression=None, number_list=None, custom_function=None, custom_parameter=None):
    operator_tuple = ('+', '-', '*', '/')
    func_dict, tmp_dict, graph, number_stack = {}, {}, [], MyStack()
    graph.append('digraph G {')
    graph.append(F'  INPUT[shape=rect label="{str_expression}"];')
    graph.append('  OUTPUT[shape=rect];')
    for i in range(len(number_list)):
        if number_list[i] not in operator_tuple:
            graph.append(F'  node_{i}[label="{number_list[i]}"];')
        else:
            graph.append(F'  node_{i}[label="{number_list[i]}" shape=square];')
        if number_list[i] not in operator_tuple:
            graph.append(F'  INPUT -> node_{i};')
    for e in number_list:
        if e not in operator_tuple and not e.isdigit() and not 'x' <= e <='z' :
            # Get functions.
            func, tmp_lst = e[0:3], []
            for e_e in e[3:]:
                if e_e.isdigit():
                    tmp_lst.append(int(e_e))
            # Calculate value of sin, cos, pow, log funciton.
            if func == 'pow':
                res = str(int(pow(tmp_lst[0], tmp_lst[1])))
                calculate_math_function(number_list, graph, func_dict, e, res, func)
            elif func == 'sin':
                res = str(int(sin(tmp_lst[0])))
                calculate_math_function(number_list, graph, func_dict, e, res, func)
            elif func == 'cos':
                res = str(int(cos(tmp_lst[0])))
                calculate_math_function(number_list, graph, func_dict, e, res, func)
            elif func == 'log':
                res = str(int(log(tmp_lst[0])))
                calculate_math_function(number_list, graph, func_dict, e, res, func)
    # Calculate the custom function.
    calculate_custom_function(number_list, operator_tuple, custom_function, custom_parameter, graph, func_dict)
    for e in number_list:
        if isfloat(e) or e.isdigit():
            number_stack.push(e)
        elif e in operator_tuple:
            number_1, number_2 = convert_numbers_into_int_or_float(number_stack.pop(), number_stack.pop())
            if e == '+':
                res = number_1 + number_2
                calculate_by_operator(number_1, number_2, e, res, func_dict, tmp_dict, number_list, graph, number_stack)
            elif e == '-':
                res = number_2 - number_1
                calculate_by_operator(number_1, number_2, e, res, func_dict, tmp_dict, number_list, graph, number_stack)
            elif e == '*':
                res = number_1 * number_2
                calculate_by_operator(number_1, number_2, e, res, func_dict, tmp_dict, number_list, graph, number_stack)
            elif e == '/':
                try:
                    res = number_2 / number_1
                except ZeroDivisionError:
                    print('0 cannot be divided! Please check the input expression.')
                    return
                calculate_by_operator(number_1, number_2, e, res, func_dict, tmp_dict, number_list, graph, number_stack)
    num_res = number_stack.pop()
    graph.append(F'  node_{len(number_list)-1} -> OUTPUT[label="="];')
    graph.append('}')
    if type(eval(num_res)) is int: num_res = int(num_res)
    else: num_res = float(num_res)
    if str_expression is None: return num_res
    else: return '\n'.join(graph)



def detection_of_bracket_matches(expression):
    bracket_stack = MyStack()
    for e in expression:
        if e == '(':
            bracket_stack.push(e)
        elif e == ')':
            if bracket_stack.is_empty(): return False
            elif bracket_stack.top() == '(':
                bracket_stack.pop()
                continue
            else: return False
        else: continue
    return True
def how_many_variable_in_custom_function(function_str_expression, custom_parameter):
    """
    Calculate how many variables in a custom function:f(x) -> 1, f(x, y) -> 2
    """
    variable_list = []
    for e in function_str_expression:
        if 'x' <= e <= 'z':
            variable_list.append(custom_parameter[e])
    return variable_list


def calculate_custom_function(number_list, operator_tuple, custom_function, custom_parameter, graph, func_dict):
    """
    Calculate the value of custom functions.
    """
    if custom_parameter is None:
        return
    elif custom_function is not None:
        for e in number_list:
            if not (e.isdigit() or e in operator_tuple or 'y' <= e <= 'z') and e[0] == 'f':
                variable_list = how_many_variable_in_custom_function(e, custom_parameter)
                res = str(custom_function(*variable_list))
                index = number_list.index(e)
                number_list[index] = res
                graph.append(F'  node_result_of_f[label="{res}"];')
                graph.append(F'  node_{index} -> node_result_of_f;')
                func_dict[index] = 'f'
            elif 'y' <= e <= 'z':
                index = number_list.index(e)
                number_list[index] = str(custom_parameter[e])
                graph.append(F'  node_result_of_{e}[label="{custom_parameter[e]}"];')
                graph.append(F'  node_{index} -> node_result_of_{e};')
                func_dict[index] = e
    else:
        for e in number_list:
            if 'x' <= e <= 'z':
                number_list[number_list.index(e)] = str(custom_parameter[e])



def calculate_math_function(number_list, graph, func_dict, e, res, func):
    index = number_list.index(e)
    number_list[index] = res
    graph.append(F'  node_result_of_{func}[label="{res}"];')
    graph.append(F'  node_{index} -> node_result_of_{func};')
    func_dict[index] = func


    
def convert_numbers_into_int_or_float(number_1, number_2):
    """
    When 2 numbers pop from the stack, they will be converted to the corresponding type.
    """
    if isfloat(number_1): number_1 = float(number_1)
    else: number_1 = int(number_1)
    if isfloat(number_2): number_2 = float(number_2)
    else: number_2 = int(number_2)
    return number_1, number_2



def my_list_remove(lst, element):
    """
    Set the first searching value to 'None'.
    """
    for i in range(len(lst)):
        if lst[i] == element:
            lst[i] = None
            break



def isfloat(s):
    """
    return True if this string is a float, otherwise False.
    """
    try:
        if s in ['+', '-', '*', '/']: return False
        int(s)
        return False
    except ValueError:
        return True



def calculate_by_operator(number_1, number_2, e, res, func_dict, tmp_dict, number_list, graph, number_stack):
    """
    Calculate the result and plot the graph.
    """
    operator_index = number_list.index(e)
    my_list_remove(number_list, e)
    number_stack.push(str(res))
    tmp_dict[res] = {}
    tmp_dict[res]['index'] = operator_index
    tmp_dict[res]['number_1'] = number_1
    tmp_dict[res]['number_2'] = number_2
    plot_stack_graph(number_1, number_2, e, operator_index, func_dict, tmp_dict, number_list, graph)



def plot_stack_graph(number_1, number_2, operator, operator_index, func_dict, tmp_dict, number_list, graph):
    """
    Plot the graph with the operator.
    """
    #operator_index: operator poped from stack.
    if str(number_1) in number_list and str(number_2) in number_list:
        index_1, index_2 = number_list.index(str(number_1)), number_list.index(str(number_2))
        if index_1 in func_dict.keys():
            graph.append(F'  node_result_of_{func_dict[index_1]} -> node_{operator_index};')
        else:
            graph.append(F'  node_{index_1} -> node_{operator_index};')
        if index_2 in func_dict.keys():
            graph.append(F'  node_result_of_{func_dict[index_2]} -> node_{operator_index};')
        else:
            graph.append(F'  node_{index_2} -> node_{operator_index};')
        my_list_remove(number_list, str(number_1))
        my_list_remove(number_list, str(number_2))
    elif str(number_1) in number_list and number_2 in tmp_dict.keys():
        index_1 = number_list.index(str(number_1))
        after_calculation_operator_index = tmp_dict[number_2]['index']
        graph.append(F'  node_{after_calculation_operator_index} -> node_{operator_index};')
        if index_1 in func_dict.keys():
            graph.append(F'  node_result_of_{func_dict[index_1]} -> node_{operator_index};')
        else:
            graph.append(F'  node_{number_list[index_1]} -> node_{operator_index};')
        my_list_remove(number_list, str(number_1))
    elif str(number_2) in number_list and number_1 in tmp_dict.keys():
        index_2 = number_list.index(str(number_2))
        after_calculation_operator_index = tmp_dict[number_1]['index']
        graph.append(F'  node_{after_calculation_operator_index} -> node_{operator_index};')
        if index_2 in func_dict.keys():
            graph.append(F'  node_result_of_{func_dict[index_2]} -> node_{operator_index};')
        else:
            graph.append(F'  node_{index_2} -> node_{operator_index};')
        my_list_remove(number_list, str(number_2))
    else:
        operator_index_1 = tmp_dict[number_1]['index']
        operator_index_2 = tmp_dict[number_2]['index']
        graph.append(F'  node_{operator_index_1} -> node_{operator_index};')
        graph.append(F'  node_{operator_index_2} -> node_{operator_index};')

class BracketDismatchError(Exception): 
    def __init__(self, msg):
        self.msg = F'Expression: \'{msg}\' has dismatched brackets, please check again.'



if __name__ == '__main__':
    str_1 = '3*(pow(2, 3)+cos(0))-f(x)'
    parse_stack = parse_str(str_1)
    graph = calculate(number_list=parse_stack, str_expression=str_1, custom_function=lambda x:x+1, custom_parameter={'x':1})
    print(graph)