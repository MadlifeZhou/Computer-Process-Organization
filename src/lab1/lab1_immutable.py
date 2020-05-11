# -*- coding: utf-8 -*- 

class Node(object):
    def __init__(self, value=None, lchild=None, rchild=None):
        self.value  = value
        self.lchild = lchild
        self.rchild = rchild
    
    def __eq__(self, other_node):
        if id(self) == id(other_node):
            return True
        else:
            lst_self  = create_none_list(self)
            lst_other = create_none_list(other_node)
            to_list(self, 0, lst_self)
            to_list(other_node, 0, lst_other)
            return lst_self == lst_other
            
    
def create_none_list(node):
    if get_size(node) == 1:
        return [None, None, None]
    else:
        return [None for _ in range((1<<get_depth(node))-1)]

def to_list(node, cntr, lst):
    if cntr <= len(lst) - 1:
        if node is not None:
            lst[cntr] = node.value
        else:
            lst[cntr] = None
            return
        to_list(node.lchild, (cntr<<1)+1, lst)
        to_list(node.rchild, (cntr<<1)+2, lst)
    else:
        return

def to_list_without_none(node):
    lst_without_none = []
    tmp_lst = create_none_list(node)
    to_list(node, 0, tmp_lst)
    for i in range(len(tmp_lst)):
        if tmp_lst[i] is not None:
            lst_without_none.append(tmp_lst[i])
    return lst_without_none

def mconcat(node_1, node_2):
    if node_2 is None:
        return node_1;
    elif node_1 is None:
        return mconcat(node_2, node_1)
    else:
        lst_node_1 = to_list_without_none(node_1)
        lst_node_2 = to_list_without_none(node_2)
        lst_node_1.extend(lst_node_2)
        return lst_node_1

def from_list(lst, index):
    if len(lst) > 0:
        if index < len(lst):
            return Node(value=lst[index], lchild=from_list(lst, (index<<1)+1), rchild=from_list(lst, (index<<1)+2))
    else:
        return None


def is_leaf(node):
    if node.lchild == None and node.rchild == None:
        return True
    else:
        return False

def get_depth(node):
    if node is None:
        return 0
    else:
        return max(get_depth(node.lchild)+1, get_depth(node.rchild)+1)


def get_size(node):
    # Get size of the binary tree.
    if node is None:
        return 0
    elif is_leaf(node):
        return 1
    else:
        return get_size(node.lchild) + get_size(node.rchild) + 1

def add_node(value, left=None, right=None):
    # Add node into the binary tree.
    return Node(value=value, lchild=left, rchild=right)

def remove_node(node, element):
    """
    Remove node from the tree.
    If the node is a leaf, it will be removed directly. Otherwise, node with its children will be all removed.
    Parameters:
        node: root of tree.
        element: the element that should be removed.
    """
    lst = [None for _ in range((1<<get_depth(node))-1)]
    to_list(node, 0, lst)
    index = lst.index(element)
    parent_index = index >> 1
    parent_element = lst[parent_index]
    find_parent(node, parent_element)

def find_parent(node, element_value):
    if node is not None:
        if node.value == element_value:
            node.lchild = None
            node.rchild = None
        find_parent(node.lchild, element_value)
        find_parent(node.rchild, element_value)
def find_node(node, element_value, fetch_list):
    if node is not None:
        if node.value == element_value:
            fetch_list.append(node.value)
        find_node(node.lchild, element_value, fetch_list)
        find_node(node.rchild, element_value, fetch_list)


def mempty():
    return None

def filter(node, func):
    lst = [None for x in range((1<<get_depth(node))-1)]
    to_list(node, 0, lst)
    new_lst = func(lst)
    return new_lst

def map_func(lst):
    for i in range(len(lst)):
        if lst[i] is not None:
            lst[i] = lst[i] << 1 + 2
def reduce_fuc(x, y):
    return x + y

def filter_func(lst):
    new_list = []
    for i in range(len(lst)):
        if lst[i] is not None and lst[i] <= 'C':
            new_list.append(lst[i])
    return new_list

def map(node, func):
    lst = [None for x in range((1<<get_depth(node))-1)]
    to_list(node, 0, lst)
    func(lst)
    return from_list(lst, 0)

def my_reduce(node, func):
    from functools import reduce
    lst = [None for x in range((1<<get_depth(node))-1)]
    to_list(node, 0, lst)
    new_list = [x for x in lst if x is not None]
    return reduce(func, new_list)

def iterator(node):
    lst = create_none_list(node)
    to_list(node, 0, lst)
    return iter(lst)

node_1 = None
node_2 = add_node(value=1, left=add_node(value=2), right=add_node(value=3, left=Node(value=4)))
lst = mconcat(node_1, node_2)
print(lst)