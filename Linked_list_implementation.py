#Node class to create new nodes for tor the linked list
#LinkedClasss intialize the head pointer for the node
#insert method is to insert a noce in a list.

class LinkedlistNode:
	def __init__(self, value, nextNode=None):
		self.value = value
		self.nextNode = nextNode
# when creating linked it contaims only header 
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

	def deleteHead(self):
		previousHead = self.head
		self.head = self.head.nextNode
		previousHead = None
			
# to delete a node we should know the position of a node to which node we should delete
	def delete(self, position):
		currentNode = self.head
		currentPosition = 0
		if position is 0:
			self.deleteHead()
			return
		while True:
			if currentPosition == position:
				previousenode.nextNode = currentNode.nextNode
				currentNode.nextNode = None
				break
			
			previousenode = currentNode
			currentNode = currentNode.nextNode
			currentPosition +=1


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
s1.delete(1)
s1.printLinkedList()



