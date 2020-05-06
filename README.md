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

- size

  Traverse a tree to get a queue full of nodes, and calculate the length of the queue is the number of nodes in the tree

- Remove

  We traverse a tree, if the node is the node we want to delete, we delete it

- to list

  Traverse a tree, store the results of traversing nodes in a queue, and extract the node values of the queue into a list, which is the result we want

- from list

  We provide a list, traverse the list, and add it to the tree in turn

- map

  Traverse a tree, and then perform a function operation on it, and change the value of the node according to the function

- Filter

  Traverse a tree, and then judge it, if it does not meet the function filter conditions, delete it, and ignore it if it meets the function conditions

- Find

  

- reduce

  Process structure elements to build a return value by speci ﬁ c functions. Traverse a tree, enter an initial state value, each time a node is traversed, the initial state value is updated according to the function, and finally the final state value is output

- Find the elements level by level

  

- Iterator

###### 





