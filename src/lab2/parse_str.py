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


"""
def parse_bracket(string):
    my_stack = MyStack()
    for e in string:
        if e == '(':
            my_stack.push(e)
        elif e == ')':
            if my_stack.top() == '(' and not my_stack.is_empty():
                my_stack.pop()
            else:
                return False
    if my_stack.is_empty(): return True
    else: return False
"""


def parse_str(expression):
    number_stack, operator_stack, i = MyStack(), MyStack(), 0
    operator_priority = {'+': 1, '-': 1, '*': 2, '/': 2, '(': -1, ')': -1}
    while (i < len(expression)):
        tmp_str = ''
        # Elements like 'sin', 'cos', 'tan' will be considered as a number.
        if expression[i] not in operator_priority.keys() and 'a' <= expression[i] <= 'z':
            # 'f' means custom functions.
            if expression[i] == 'p' or expression[i] == 'f':
                while expression[i] not in list(operator_priority.keys())[0:4]:
                    tmp_str += expression[i]
                    i += 1
                    if i == len(expression): break
            else:
                while expression[i] not in operator_priority.keys():
                    tmp_str += expression[i]
                    i += 1
                    if i == len(expression): break
            number_stack.push(tmp_str)
            if i == len(expression): break
        if expression[i].isdigit():
            # Digit will be pushed into stack directly.
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
    number_stack.push(operator_stack.pop())
    return number_stack._lst


def calculate_custom_function(number_list, operator_tuple, custom_function, custom_parameter):
    if custom_function is None and custom_parameter is None:
        return
    else:
        for e in number_list:
            if not (e.isdigit() or e in operator_tuple):
                number_list[number_list.index(e)] = str(custom_function(custom_parameter))


def calculate(number_list, custom_function=None, custom_parameter=None):
    operator_tuple = ('+', '-', '*', '/')
    number_stack = MyStack()
    for e in number_list:
        if e not in operator_tuple and not e.isdigit():
            # Get functions.
            func = e[0:3]
            tmp_lst = []
            for e_e in e[3:]:
                if e_e.isdigit():
                    tmp_lst.append(int(e_e))
            # Calculate value of sin, cos, pow, log funciton.
            if func == 'pow':
                number_list[number_list.index(e)] = str(int(pow(tmp_lst[0], tmp_lst[1])))
            elif func == 'sin':
                number_list[number_list.index(e)] = str(int(sin(tmp_lst[0])))
            elif func == 'cos':
                number_list[number_list.index(e)] = str(int(cos(tmp_lst[0])))
            elif func == 'log':
                number_list[number_list.index(e)] = str(int(log(tmp_lst[0])))
    # Calculate the custom function.
    calculate_custom_function(number_list, operator_tuple, custom_function, custom_parameter)
    for e in number_list:
        if e.isdigit():
            number_stack.push(e)
        elif e in operator_tuple:
            operator_1 = int(number_stack.pop())
            operator_2 = int(number_stack.pop())
            if e == '+':
                number_stack.push(str(operator_1 + operator_2))
            elif e == '-':
                number_stack.push(str(operator_2 - operator_1))
            elif e == '*':
                number_stack.push(str(operator_1 * operator_2))
            else:
                number_stack.push(str(operator_2 / operator_1))
    return number_stack.pop()
