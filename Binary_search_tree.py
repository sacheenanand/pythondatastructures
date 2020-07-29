class Node:
    def __init__(self, data):
        self.data = data
        self.rightchild = None
        self.leftchild = None

class Tree:
    def __init__(self):
        self.rootnode = None

    def insert(self, dat):

        node = Node(data)
        if self.rootnode is None:
            self.rootnode = node
        else:
            current = self.rootnode

        
        parent = None
        while True:
            parent = current
            if current.data < node.data:
                current = current.leftchild
                if current is None:
                    parent.leftchild = node
                    return
            else:

                current = current.rightchild
                if current is None:
                    parent.rightchild = node
                    return







    