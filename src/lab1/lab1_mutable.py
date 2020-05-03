# coding=utf-8
"""
Author: Zhou Guancheng
Date: 03-05-2020
Title: A Immutable Binary Tree
"""
import math


class Node(object):
    """Node class, the basic structure of a Tree"""

    def __init__(self, elem=None, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

    def height(self):
        return 1 + max(self.lchild)


class Tree(object):
    """Tree"""

    '''Initial the Tree'''

    def __init__(self, root=Node(None)):
        self.root = root
        self.myList=[]
    '''Add a Node to Tree'''

    def addNode(self, elem):
        myQueue = []
        new_node = Node(elem)
        # 如果树是空的，则对根节点赋值
        if self.root.elem is None:
            self.root = new_node
            return
        # 如果树不是空的，则使用层次遍历添加节点
        myQueue.append(self.root)
        while myQueue:
            tree_node = myQueue.pop(0)
            if tree_node.lchild is None:
                tree_node.lchild = new_node
                return
            elif tree_node.rchild is None:
                tree_node.rchild = new_node
                return
            if tree_node.lchild is not None:
                myQueue.append(tree_node.lchild)
            if tree_node.rchild is not None:
                myQueue.append(tree_node.rchild)

    '''Output the size of tree'''

    def size(self):
        if self.root.elem is None:
            return 0
        else:
            return len(self.level_queue(self.root))

    '''remove the given leaf of tree'''

    def remove_leaf(self, elem):
        if self.root is None:
            return
        myQueue = []
        node = self.root
        if node.elem == elem and (node.lchild is not None or node.lchild is not None):
            print("the element you choose is not the leaf")
            return
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            left = node.lchild
            right = node.rchild
            if (left is not None and left.elem == elem and (left.lchild is None
                                                            and left.rchild is None)):
                node.lchild = None
                return
            elif (right is not None and right.elem == elem and (right.lchild is None
                                                                and right.rchild is None)):
                node.rchild = None
                return
            elif left is not None and left.elem == elem and (left.lchild is not None
                                                             or left.rchild is not None):
                print("the element you choose is not the leaf")
                return
            elif right is not None and right.elem == elem and (right.lchild is not None
                                                               or right.rchild is not None):
                print("the element you choose is not the leaf")
                return
            if left is not None:
                myQueue.append(node.lchild)
            if right is not None:
                myQueue.append(node.rchild)
        print("we can not find the elem")

    '''Convert all the nodes of Tree to a list'''

    def to_list(self):
        if self.root.elem is None:
            return []
        lst = []
        result = self.level_queue(self.root)
        for e in result:
            if e.elem is not None:
                lst.append(e.elem)
        return lst

    '''Convert all the element of List to a Tree'''

    def from_list(self, lst):
        # if it is not an Empty Tree, Clear the whole tree
        if self.root.elem is not None:
            self.root = None
        self.root = Node()
        for e in lst:
            self.addNode(e)

    '''Implement a Function on all the nodes of Tree'''

    def map(self, f):
        if self.root.elem is None:
            return
        nodes = self.level_queue(self.root)
        for e in nodes:
            e.elem = f(e.elem)

    def reduce(self, f, initial_state):
        if self.root.elem is None:
            return initial_state
        lst = self.level_queue(self.root)
        state = initial_state
        for e in lst:
            state = f(state, e.elem)
        return state

    '''Find the Elements which fit the function'''

    def find(self, f):
        lst = self.to_list()
        for e in lst:
            if not f(e):
                lst.remove(e)
        return lst

    '''Search the elements of Tree level by level'''

    def level_queue(self, root):
        """利用队列实现树的层次遍历"""
        if root.elem is None:
            return None
        myQueue = []
        result = []
        node = root
        myQueue.append(node)
        result.append(node)
        while myQueue:
            node = myQueue.pop(0)
            # print(node.elem)
            if node.lchild is not None:
                myQueue.append(node.lchild)
                result.append(node.lchild)
            if node.rchild is not None:
                myQueue.append(node.rchild)
                result.append(node.rchild)
        return result

    def findMax(self):
        lst = self.front_stack(self.root)
        return max(lst)

    def findMin(self):
        lst = self.front_stack(self.root)
        return min(lst)

    def pre_order_search(self, root):
        """利用递归实现树的先序遍历"""
        if root is None:
            return []
        print(root.elem)
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)

    def in_order_search(self, root):
        """利用递归实现树的中序遍历"""
        if root is None:
            return
        self.middle_digui(root.lchild)
        print(root.elem)
        self.middle_digui(root.rchild)

    def post_order_search(self, root):
        """利用递归实现树的后序遍历"""
        if root is None:
            return
        self.later_digui(root.lchild)
        self.later_digui(root.rchild)
        print(root.elem)

    def pre_order_search_stack(self, root):
        """利用堆栈实现树的先序遍历"""
        if root is None:
            return
        myStack = []
        all_nodes = []
        node = root
        while node or myStack:
            while node:  # 从根节点开始，一直找它的左子树
                print(node.elem)
                all_nodes.append(node.elem)
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()  # while结束表示当前节点node为空，即前一个节点没有左子树了
            node = node.rchild  # 开始查看它的右子树
        return all_nodes

    def in_order_search_stack(self, root):
        """利用堆栈实现树的中序遍历"""
        if root is None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:  # 从根节点开始，一直找它的左子树
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()  # while结束表示当前节点node为空，即前一个节点没有左子树了
            print(node.elem)
            node = node.rchild  # 开始查看它的右子树

    def post_order_search_stack(self, root):
        """利用堆栈实现树的后序遍历"""
        if root is None:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1:  # 这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            node = myStack1.pop()
            if node.lchild:
                myStack1.append(node.lchild)
            if node.rchild:
                myStack1.append(node.rchild)
            myStack2.append(node)
        while myStack2:  # 将myStack2中的元素出栈，即为后序遍历次序
            print(myStack2.pop().elem)

    def __iter__(self):
        self.myList = self.level_queue(self.root)
        if self.myList is not None:
            self.myList.pop(0)
        return Tree(self.root)

    def __next__(self):
        if self.root.elem is None:
            raise StopIteration
        tmp = self.root.elem
        self.root = self.myList.pop(0)
        print(self.root.elem)
        return tmp


if __name__ == '__main__':
    lst = Tree()
    lst.from_list([1, 2, 3])
    add = lambda st, e: st + e
    print(lst.reduce(add, 0))
