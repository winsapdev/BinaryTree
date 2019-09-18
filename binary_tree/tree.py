class Node():
	value = None
	left = None
	right = None

	def __init__(self, nilai):
		self.value = nilai

	# for debug
	def __str__(self):
		return "<Node with val {}>".format(self.value);

	def get_value(self):
		return self.value


class BinaryTree():

	root = None

	def add_node(self, node):
		if self.root is None:
			self.root = Node(node)
		else:
			self.insert_node(self.root, Node(node))

	def insert_node(self, parent, node):
		if parent.get_value() > node.get_value():
			if parent.left is None:
				parent.left = node
			else:
				self.insert_node(parent.left, node)	
		else:
			if parent.right is None:
				parent.right = node
			else:
				self.insert_node(parent.right, node)


	def preorder(self, root):
		if root is not None:
			print(str(root.value)+" ", end="")
			self.preorder(root.left)
			self.preorder(root.right)

	def postorder(self, root):
		if root is not None:
			self.postorder(root.left)
			self.postorder(root.right)
			print(str(root.value)+" ", end="")

	def inorder(self, root):
		if root is not None:
			self.inorder(root.left)
			print(str(root.value)+" ", end="")
			self.inorder(root.right)

	def leaf_count(self, root):
		if root is None:
			return 0
		if root.left is None and root.right is None:
			return 1
		else:
			return self.leaf_count(root.left) + self.leaf_count(root.right)

	def max_depth(self, root):
		if root is None:
			return 0
		else:
			ldepth = self.max_depth(root.left)
			rdepth = self.max_depth(root.right)

			if ldepth>rdepth:
				return ldepth+1
			else:
				return rdepth+1
