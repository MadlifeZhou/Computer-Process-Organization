# coding=utf-8

from lab1_mutable import *
from hypothesis import given
import hypothesis.strategies as st

tree = Tree(Node())
print(tree.to_list())
