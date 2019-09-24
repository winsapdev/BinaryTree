import sys
from binary_tree.tree import BinaryTree



if __name__ == '__main__':
	bt = BinaryTree()
	data = list(sys.argv[1].split(","))
	for i in data:
		bt.add_node(i)
	

	print("inorder: ")
	bt.inorder(bt.root)	
	print("")
	print("")
	print("preorder: ")
	bt.preorder(bt.root)	
	print("")
	print("")
	print("postorder: ")
	bt.postorder(bt.root)	
	print("")
	print("")
	print("leaf count: {}".format(bt.leaf_count(bt.root)))
	print("height of tree: {}".format(bt.max_depth(bt.root)))
	print("max level of tree: {}".format(bt.max_depth(bt.root)-1))
