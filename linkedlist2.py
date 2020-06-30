#now we want to create a node so that value is inserted

class LinkedlistNode:
	def __init__(self, value, nextNode=None):
		self.value = value
		self.nextNode = nextNode
class Linkedlist:
	def __init__(self, head=None):
		self.head = head
def insert(self, value):
	node = LinkedlistNode(value)
	if self.head is Node:
		self.head = node
    	return
#currentnode = self.head

    while True:
    	if currentnode.nextNode is None:
    		currentnode.nextNode = node
    		break
    	currentnode = currentnode.nextNode
def printLinkedlist(self):
	currentnode = self.head
	while currentnode is not None:
		print currentnode.value, "->"
		currentnode =currentnode.nextNode
	print("None")


ll = Linkedlist()
ll.printLinkedlist()
ll.insert("3")
ll.printLinkedlist()



