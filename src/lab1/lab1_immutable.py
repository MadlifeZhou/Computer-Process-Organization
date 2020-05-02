# coding=utf-8

class Node(object):
    """节点类"""

    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

    def height(self):
        return 1 + max(self.lchild)


class Tree(object):
    """树类"""

    def __init__(self, root=Node()):
        self.root = root

    def addNode(self, elem):
        myQueue = []
        new_node = Node(elem)
        # 如果树是空的，则对根节点赋值
        if self.root.elem == -1:
            self.root = new_node
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
            elif tree_node.lchild is not None:
                myQueue.append(node.lchild)
            elif tree_node.rchild is not None:
                myQueue.append(node.rchild)

    def size(self):
        return len(self.level_queue(self.root))

    def front_digui(self, root):
        """利用递归实现树的先序遍历"""
        if root == None:
            return []
        print(root.elem)
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)

    def front_search(self, root):
        """利用递归实现树的先序遍历"""
        if root == None:
            return []
        print(root.elem)
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)

    def front_digui(self, root):
        """利用递归实现树的先序遍历"""
        if root == None:
            return []
        print(root.elem)
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)

    def remove_leaf(self, root, elem):
        if root == None:
            return
        myQueue = []
        result = []
        node = root
        if node.elem == elem and (node.lchild is not None or node.lchild is not None):
            print("the element you choose is not the leaf")
            return
        myQueue.append(node)
        result.append(node)
        while myQueue:
            node = myQueue.pop(0)
            left = node.lchild
            right = node.rchild
            if (left is not None and left.elem == elem and (node.lchild.lchild is None
                                                            and node.lchild.rchild is None)):
                left = None
                return
            elif (right is not None and right.elem == elem and (node.rchild.lchild is None
                                                                and node.rchild.rchild is None)):
                right = None
                return
            elif left is not None and left.elem == elem and (left.lchild is not None
                                                             or left.rchild is not None):
                print("the element you choose is not the leaf")
                return
            elif right is not None and right.elem == elem and (right.lchild is not None
                                                               or right.rchild is not None):
                print("the element you choose is not the leaf")
                return
            if node.lchild is not None:
                myQueue.append(node.lchild)
                result.append(node.lchild)
            if node.rchild is not None:
                myQueue.append(node.rchild)
                result.append(node.lchild)

    def middle_digui(self, root):
        """利用递归实现树的中序遍历"""
        if root == None:
            return
        self.middle_digui(root.lchild)
        print(root.elem)
        self.middle_digui(root.rchild)

    def later_digui(self, root):
        """利用递归实现树的后序遍历"""
        if root == None:
            return
        self.later_digui(root.lchild)
        self.later_digui(root.rchild)
        print(root.elem)

    def front_stack(self, root):
        """利用堆栈实现树的先序遍历"""
        if root == None:
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

    def middle_stack(self, root):
        """利用堆栈实现树的中序遍历"""
        if root == None:
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

    def later_stack(self, root):
        """利用堆栈实现树的后序遍历"""
        if root == None:
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

    def level_queue(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        myQueue = []
        result = []
        node = root
        myQueue.append(node)
        result.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.elem)
            if node.lchild != None:
                myQueue.append(node.lchild)
                result.append(node.lchild)
            if node.rchild != None:
                myQueue.append(node.rchild)
                result.append(node.lchild)
        return result

    def findMax(self):
        lst = self.front_stack(self.root)
        return max(lst)

    def findMin(self):
        lst = self.front_stack(self.root)
        return min(lst)


if __name__ == '__main__':
    """主函数"""
    # elems = range(10)           #生成十个数据作为树节点
    # tree = Tree()          #新建一个树对象
    # for elem in elems:
    #     tree.add(elem)           #逐个添加树的节点

    node = Node(1, Node(2, Node(4)), Node(3, None, Node(5)))
    tree = Tree(node)
    # print("队列实现层次遍历:")
    # tree.level_queue(tree.root)

    # print('\n\n递归实现先序遍历:')
    # tree.front_digui(tree.root)
    # print('\n递归实现中序遍历:')
    # tree.middle_digui(tree.root)
    # print('\n递归实现后序遍历:')
    # tree.later_digui(tree.root)
    #
    # print('\n\n堆栈实现先序遍历:')
    # tree.front_stack(tree.root)
    # print('\n堆栈实现中序遍历:')
    # tree.middle_stack(tree.root)
    # print('\n堆栈实现后序遍历:')
    # tree.later_stack(tree.root)

    tree.addNode(100)
    print("队列实现层次遍历:")
    tree.level_queue(tree.root)
    tree.remove_leaf(tree.root, 1)
    print("队列实现层次遍历:")
    tree.level_queue(tree.root)
