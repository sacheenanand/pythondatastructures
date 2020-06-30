class Linkedlist:
	def __init__(self, value, nextNode=None):
		self.value = value
		self.nextNode = nextNode

node1 = Linkedlist("7")
node2 =Linkedlist("10")
node3 = Linkedlist("11")
node4 = Linkedlist("19")


node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4

currentnode = node1

while True:
	print currentnode.value, "->"
	if currentnode.nextNode is None:
		print("None")
		break

	currentnode = currentnode.nextNode
