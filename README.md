# Binary Tree
simple implementation of binary tree in python

## Usage

```python
from binary_tree.tree import BinaryTree

bt = BinaryTree()

bt.add_node(4)
bt.add_node(2)
bt.add_node(1)
bt.add_node(8)
```
or you can use my example file

```bash
python main.py 5,3,6,8,7,2,9
```

### Supported Method
`add_node(number)` : add new node to the tree 
`inorder(root)` : inorder traversal 
`preorder(root)` : preorder traversal 
`postorder(root)` : postorder traversal 
`leaf_count(root)` : get leaf count from the tree 
`max_depth(root)` : height of the tree (max level of the tree is height-1)


