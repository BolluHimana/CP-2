class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        if self.root.value==new_val:
            return False
        elif new_val<self.root.value:
            if self.root.left:
                return self.root.left.insert(new_val)
            else:
                self.root.left=Node(new_val)
                return True
        else:
            if self.root.right:
                return self.root.right.insert(new_val)
            else:
                self.root.right=Node(new_val)
                return True

    def printSelf(self):
        # Your code goes here
        pass
        
    def search(self, find_val):
        if find_val==self.root.value:
            return True
        elif find_val<self.root.value:
            if self.root.left:
                return self.root.left.search(find_val)
            else:
                return False
        else:
            if self.root.right:
                return self.root.right.search(find_value)
            else:
                return False
