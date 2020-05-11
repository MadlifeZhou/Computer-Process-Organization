from lab1_immutable import *
import unittest
from hypothesis import given
import hypothesis.strategies as st

class TestImmutableMutableList(unittest.TestCase):
    def test_size(self):
        self.assertEqual(get_size(None), 0)
        self.assertEqual(get_size(Node(0)), 1)
        self.assertEqual(get_size(Node(value=1, lchild=add_node(value=2))), 2)
    
    def test_get_depth(self):
        self.assertEqual(get_depth(Node(value=1)), 1)
        self.assertEqual(get_depth(Node(value=1, lchild=Node(value=2), rchild=Node(value=3))), 2)
        self.assertEqual(get_depth(add_node(value=1, left=add_node(value=2, left=add_node(value=3)))), 3)

    def test_create_none_list(self):
        self.assertEqual(create_none_list(Node(value=1)), [None, None, None])
    
    def test_to_list(self):
        node_1 = Node(value=1)
        lst_node_1 = create_none_list(node_1)
        to_list(node_1, 0, lst_node_1)
        self.assertEqual(lst_node_1, [1, None, None])

        node_2 = add_node(value=1, left=add_node(value=2), right=add_node(value=3, left=Node(value=4)))
        lst_node_2 = create_none_list(node_2)
        to_list(node_2, 0, lst_node_2)
        self.assertEqual(lst_node_2, [1, 2, 3, None, None, 4, None])

        node_3 = None
        lst_node_3 = create_none_list(node_3)
        to_list(node_3, 0, lst_node_3)
        self.assertEqual(lst_node_3, [])

    def test_to_list_without_none(self):
        node_1 = Node(value=1)
        node_2 = add_node(value=1, left=add_node(value=2), right=add_node(value=3, left=Node(value=4)))
        self.assertEqual(to_list_without_none(node_1), [1])
        self.assertEqual(to_list_without_none(node_2), [1, 2, 3, 4])

    def test_mconcat(self):
        node_1 = Node(value=1)
        node_2 = add_node(value=1, left=add_node(value=2), right=add_node(value=3, left=Node(value=4)))
        self.assertEqual(mconcat(node_1, node_2), [1, 1, 2, 3, 4])


    def test_from_list(self):
        list_1 = [1, 2, 3, None, None, 4, None]
        list_2 = []
        list_3 = [1]
        node_1 = add_node(value=1, left=add_node(value=2), right=add_node(value=3, left=Node(value=4))) 
        self.assertEqual(from_list(list_1, 0), node_1)
        self.assertEqual(from_list(list_2,0), None)
        self.assertEqual(from_list(list_3, 0), Node(value=1))

    def test_add_node(self):
        self.assertEqual(Node(1), add_node(1))
        self.assertEqual(Node(1, lchild=Node(2)), add_node(1, left=add_node(2)))
    def test_find_node(self):
        node_1 = add_node(value=1, left=add_node(value=2), right=add_node(value=3, left=Node(value=4)))
        fetch_list = []
        find_node(node_1, 2, fetch_list)
        self.assertEqual(fetch_list, [2])
    
    def test_remove_node(self):
        node = Node(1, lchild=Node(2))
        remove_node(node, 2)
        self.assertEqual(node, Node(1))

    def test_iterator(self):
        node = add_node(value=1, left=add_node(value=2), right=add_node(value=3, left=Node(value=4)))
        iter_lst = []
        it = iterator(node)
        while True:
            try:
                x = next(it)
                iter_lst.append(x)
            except StopIteration:
                break
        self.assertEqual(iter_lst, [1, 2, 3, None, None, 4, None])

    @given(node=st.lists(st.integers()))
    def test_equality(self, node):
        tree = from_list(node, 0)
        new_lst = create_none_list(tree)
        to_list(tree, 0, new_lst)
        lst = []
        for i in range(len(new_lst)):
            if new_lst[i] != None:
                lst.append(new_lst[i])
        self.assertEqual(lst, node)

    @given (lst=st.lists(st.integers()))
    def test_monoid_identity(self, lst):
        tree = from_list(lst, 0)
        self.assertEqual(mconcat(tree, None), tree)
        self.assertEqual(mconcat(None, tree), tree)
if __name__ == '__main__':
    unittest.main()