Immutable Tree  
The functions of **Immutable Tree** are as follow:  
* add_node  
Add a node into a tree. Each node's position should be specified manually in this structure.
* get_depth  
Return the depth of a full binary tree.
* create_none_list  
Return a list that every element is `None`.
* to_list  
Return a list which can represent a binary tree.  
* from_list
Return a binary tree according to the given list.  
* get_size  
Return the number of a binary tree.  
* remove_node  
Remove the specified node in the binary tree. If the node is a leaf, it will be removed directly. Otherwise, node with its children will be all removed.
* find_node  
Specified element will be found and stored into a list.
* filter  
Filter the element in the binary tree according to the specified function.  
* map  
Map the element in the binary tree according to the specified function.
* my_reduce  
The binary tree will be converted to the corresponding list and reduce the every element.
* iterator  
Return a iterator of this structure.

### Work Demonstration
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