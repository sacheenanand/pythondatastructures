__author__ = 'sanand'

# To implement reverse Linked we need 3 nodes(curr, prev and next) we are changing only the pointers here.

class node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class LinkedList:
    def __init__(self, head):
        self.head = head


    def reverse(self):
        current = head
        prev = None

        while True:
            next = current.nextNode
            current.nextNode = prev
            prev = current
            current = next
        return prev