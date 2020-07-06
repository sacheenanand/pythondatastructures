#Node class to create new nodes for tor the linked list
#LinkedClasss intialize the head pointer for the node
#insert method is to insert a noce in a list.

class LinkedlistNode:
	def __init__(self, value, nextNode=None):
		self.value = value
		self.nextNode = nextNode

class Linkedlist:
	def __init__(self, head=None):
		self.head = head

	def insert(self, value):
		self.value = value
		node = LinkedlistNode(value)
		if self.head is None:
			self.head = node
			return 
		currentNode = self.head

		while  True:
			if currentNode.nextNode is None:
				currentNode.nextNode = node
				break
			currentNode = currentNode.nextNode

	def printLinkedList(self):
		currentNode = self.head
		while currentNode is not None:
			print currentNode.value, "->",
			currentNode = currentNode.nextNode
		print "None"

s1 = Linkedlist()
s1.printLinkedList()
s1.insert("2")
s1.printLinkedList()
s1.insert("39")
s1.printLinkedList()
s1.insert("99")
s1.printLinkedList()



