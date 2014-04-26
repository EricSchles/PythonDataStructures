class Node:
	left,right,cargo = None,None,0

	def __init__(self,cargo):
		self.left = None
		self.right = None
		self.cargo = cargo

	def __str__(self):
		return str(self.cargo)

class Tree:

	def __init__(self,cargo=0):
		self.root = Node(cargo)

	def addNode(self,cargo):
		curr = self.root
		while curr != None:
			if curr.left == None:
				node = Node(cargo)
				curr.left = node
				break
			elif curr.right == None:
				node = Node(cargo)
				curr.right = node
				break
			else:
				curr = curr.left
				

def inorderTraversal(tree):
	if tree == None: return
	inorderTraversal(tree.left)
	print tree.cargo,
	inorderTraversal(tree.right)

def preorderTraversal(tree):
	if tree == None: return
	print tree.cargo,
	preorderTraversal(tree.left)
	preorderTraversal(tree.right)

def postorderTraversal(tree):
	if tree == None: return
	postorderTraversal(tree.left)
	postorderTraversal(tree.right)
	print tree.cargo,


