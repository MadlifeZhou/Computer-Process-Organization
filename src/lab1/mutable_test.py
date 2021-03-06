# coding=utf-8

from lab1_mutable import *
from hypothesis import given
import hypothesis.strategies as st
import unittest


class TestMutableList(unittest.TestCase):
    def test_size(self):
        self.assertEqual(Tree().size(), 0)
        self.assertEqual(Tree(Node('a')).size(), 1)
        self.assertEqual(Tree(Node('a', Node('b'))).size(), 2)

    def test_to_list(self):
        self.assertEqual(Tree().to_list(), [])
        self.assertEqual(Tree(Node('a')).to_list(), ['a'])
        self.assertEqual(Tree(Node('a', Node('b'))).to_list(), ['a', 'b'])

    def test_remove(self):
        self.assertEqual(Tree().remove(1),None)
        tree = Tree()
        tree.from_list([1])
        self.assertEqual(tree.remove(1),None)
        tree.from_list([1,2,3,4,5])
        tree.remove(4)
        self.assertEqual(tree.to_list(), [1,2,3,5])

    def test_from_list(self):
        test_data = [[], ['a'], ['a', 'b']]
        for e in test_data:
            lst = Tree()
            lst.from_list(e)
            self.assertEqual(lst.to_list(), e)

    def test_addNode(self):
        lst = Tree()
        self.assertEqual(lst.to_list(), [])
        lst.addNode('a')
        self.assertEqual(lst.to_list(), ['a'])
        lst.addNode('b')
        self.assertEqual(lst.to_list(), ['a', 'b'])

    def test_map(self):
        lst = Tree()
        lst.map(str)
        self.assertEqual(lst.to_list(), [])

        lst = Tree()
        lst.from_list([1, 2, 3])
        lst.map(str)
        self.assertEqual(lst.to_list(), ["1", "2", "3"])

    def test_reduce(self):

        # sum of empty list
        lst = Tree()
        self.assertEqual(lst.reduce(lambda st, e: st + e, 0), 0)

        # sum of list
        lst = Tree()
        lst.from_list([1, 2, 3])
        self.assertEqual(lst.reduce(lambda st, e: st + e, 0), 6)

        # size
        test_data = [[], ['a'], ['a', 'b']]
        for e in test_data:
            lst = Tree()
            lst.from_list(e)
            self.assertEqual(lst.reduce(lambda st, _: st + 1, 0), lst.size())

    def test_find(self):
        lst = Tree()
        self.assertEqual(lst.find(lambda x: x % 2), None)

        lst = Tree()
        lst.from_list([1, 2, 3, 4, 5, 6])
        self.assertEqual(lst.find(lambda x: x % 2), [2, 4, 6])

    def test_filter(self):
        tree = Tree()
        tree.filter(lambda x: x % 2)
        self.assertEqual(tree.to_list(), [])

        tree = Tree()
        tree.from_list([2, 4, 6, 1, 3, 5, 7])
        tree.filter(lambda x: x % 2)
        self.assertEqual(tree.to_list(), [2, 4, 6])

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        lst = Tree()
        lst.from_list(a)
        b = lst.to_list()
        self.assertEqual(a, b)

    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self, a):
        lst = Tree()
        lst.from_list(a)
        self.assertEqual(lst.size(), len(a))

    def test_iter(self):
        x = [1, 2, 3]
        lst = Tree()
        lst.from_list(x)
        tmp = []
        for e in x:
            tmp.append(e)
        self.assertEqual(x, tmp)
        self.assertEqual(lst.to_list(), tmp)
        i = iter(Tree())
        self.assertRaises(StopIteration, lambda: next(i))
