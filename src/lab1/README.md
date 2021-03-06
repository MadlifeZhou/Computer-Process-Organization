# Computer-Process-Organization
HDU-ITMO Computer Process Organization labtoray work

Group Name: **JIDI**

Group Member: 

- **Wang Jiayi**
- **Zhou Guancheng** (ID: 192050193)

## Lab1 

Variant:  **3**

### Variant Description

Our task is to use Python to implement two binary trees-immutable type and mutable type.  Both of these trees must have the following functions: adding nodes, deleting nodes, calculating the number of nodes, conversion from and to python lists, finite element by speci ﬁ c predicate, map structure by speci ﬁ c function, structure by speci ﬁ c function, iterator

### Synopsis 

#### Mutable Tree

The mutable tree must first define a node class to store the left and right children and the value of the node. Then define a tree class and introduce nodes into the tree. We write the method of this tree in the tree class, then we define a tree, and we can call all methods of the tree to operate it.

### Explanation of taken design decisions and analysis

#### Mutable Tree

The functions of **mutable tree** are as follows：

- addNode

  We first traverse the nodes of a tree layer by layer, in order to find which node has an empty child node, if we find an empty child node, we need to insert the inserted node.

  ![image-20200511090420052](https://tva1.sinaimg.cn/large/007S8ZIlly1geo8hirou6j30gy07w0te.jpg)

- size

  Traverse a tree to get a queue full of nodes, and calculate the length of the queue is the number of nodes in the tree

  ![image-20200511091436656](https://tva1.sinaimg.cn/large/007S8ZIlly1geo8s7nyuzj30gt08074x.jpg)

- Remove

  We traverse a tree, if the node is the node we want to delete, we delete it

  ![image-20200511094313080](https://tva1.sinaimg.cn/large/007S8ZIlgy1geo9lunjj9j30i507wq3n.jpg)

- to list

  Traverse a tree, store the results of traversing nodes in a queue, and extract the node values of the queue into a list, which is the result we want

  ![image-20200511091524097](https://tva1.sinaimg.cn/large/007S8ZIlgy1geo8swpvwhj30in07t0tg.jpg)

- from list

  We provide a list, traverse the list, and add it to the tree in turn

  ![image-20200511091604547](https://tva1.sinaimg.cn/large/007S8ZIlgy1geo8tlzulmj30jb07smxw.jpg)

- map

  Traverse a tree, and then perform a function operation on it, and change the value of the node according to the function

  ![image-20200511091637165](https://tva1.sinaimg.cn/large/007S8ZIlgy1geo8u64jucj30im07tt9f.jpg)

- Filter

  Traverse a tree, and then judge it, if it does not meet the function filter conditions, delete it, and ignore it if it meets the function conditions

  ![image-20200511091712464](https://tva1.sinaimg.cn/large/007S8ZIlgy1geo8usheppj30kg07xgmd.jpg)

- Find

  Traverse a tree, use a function to judge each node, if the condition is met, add its value to a list, and return to a list after the traversal is completed, this list is the value of all nodes that meet the function condition

  ![image-20200511091731622](https://tva1.sinaimg.cn/large/007S8ZIlgy1geo8v4g4j6j30j407paas.jpg)

- reduce

  Process structure elements to build a return value by speci ﬁ c functions. Traverse a tree, enter an initial state value, each time a node is traversed, the initial state value is updated according to the function, and finally the final state value is output.

  ![image-20200511091756505](https://tva1.sinaimg.cn/large/007S8ZIlgy1geo8vjsbxqj30j707zmxw.jpg)

- Iterator

  First record the root node value, store each node in a list using hierarchical traversal, then traverse the list, and then take the next node value in sequence to complete the iterator traversal.
  
  ![image-20200511091822916](https://tva1.sinaimg.cn/large/007S8ZIlgy1geo8w0neolj30iz07y750.jpg)

### Immutable Tree 

The functions of **Immutable Tree** are as follow:  

* add_node 

  Add a node into a tree. Each node's position should be specified manually in this structure.</br><br/>
  ![add_node](https://tva1.sinaimg.cn/large/007S8ZIlly1geoihrqlboj30x2084q3n.jpg)
* get_depth 

  Return the depth of a full binary tree.</br><br/>
  ![get_depth](https://tva1.sinaimg.cn/large/007S8ZIlly1geoilm632dj30wy082t9g.jpg)
* create_none_list 

  Return a list that every element is `None`.</br><br/>
  ![create_none_list](https://tva1.sinaimg.cn/large/007S8ZIlly1geoinokp8nj30wy082gmd.jpg)
* to_list 

  Return a list which can represent a binary tree.</br><br/> 
  ![to_list](https://tva1.sinaimg.cn/large/007S8ZIlly1geoiopset2j30wy082gmc.jpg)
* from_list

  Return a binary tree according to the given list. </br><br/> 
  ![from_list](https://tva1.sinaimg.cn/large/007S8ZIlly1geoiphodkaj30wy082t9g.jpg)
* get_size 

  Return the number of a binary tree. </br><br/> 
  ![get_size](https://tva1.sinaimg.cn/large/007S8ZIlly1geoiqg5vpwj30wy082js4.jpg)
* remove_node 

  Remove the specified node in the binary tree. If the node is a leaf, it will be removed directly. Otherwise, node with its children will be all removed.</br><br/>
  ![remove_node](https://tva1.sinaimg.cn/large/007S8ZIlly1geoir7tcgej30wy082t9g.jpg)
* find_node 

  Specified element will be found and stored into a list.</br><br/>
  ![find_node](https://tva1.sinaimg.cn/large/007S8ZIlly1geoirz02v0j30wy082wf8.jpg)

* iterator 

  Return a iterator of this structure.</br><br/>
  ![iterator](https://tva1.sinaimg.cn/large/007S8ZIlly1geoitmnegmj30wy0823z8.jpg)

* equality  
  Test this structure's equality.</br><br/>
  ![equality](https://tva1.sinaimg.cn/large/007S8ZIlly1geoiw9cse1j30wy082js4.jpg)

* monoid  
  Test this structure's monoid.
  </br><br/>
  ![monoid](https://tva1.sinaimg.cn/large/007S8ZIlly1geoiwz3qzwj30wy082751.jpg)

### Contribution Summary

**Zhou** completed the development of the mutable tree class and finished writing its test class. **Wang** completed the development of the mutable tree class and completed the writing of its test class.

### Work Demonstration

For **mutable tree**, we define a tree class, we can use it

```python
from lab1_mutable import *
tree = Tree()
tree.from_list([1,2,3,4,5])
print(tree.to_list())
```

Then we could get output in console

```shell
$ [1,2,3,4,5]
```

For test class, we use pycharm to develop it . if you want to test a function of mutable tree, you can click  **play** icon to run a test for a function

<!--![image-20200506152705449](https://github.com/MadlifeZhou/Computer-Process-Organization/blob/master/test.jpg)-->

**For immutable tree**

A binary tree is created as follow:

```python
from lab1_immutable import *
#Create a binary tree with 4 nodes.
tree = add_node(value=1, left=add_node(value=2), right=add_node(value=3, left=Node(value=4)))
#Create a empty list to store the binary tree.
lst = create_none_list(tree)
#Convert the binary tree to list.
to_list(tree, 0, lst)
#Print this list.
print(lst)
```

We can see the output from the command line.

```shell
$ [1, 2, 3, None, None, 4, None]
```

From above, this list correctly reflects the structure of the binary tree.

### Conclusion

In this experiment, I completed the preparation and production of mutable tree, implemented addNode, remove an element, size, from and to python lists, ﬁ nd, filerdata, map, reduce, iterator methods. And passed all its tests. Deepen the understanding of Python and the understanding of data structure





###### 





