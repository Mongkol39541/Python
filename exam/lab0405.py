"""Create BSTNode​"""
class BSTNode:
    """Create BSTNode​​"""
    def __init__(self, data):
        """Create BSTNode"""
        self.data = data
        self.left = None
        self.right = None
    def get_data(self):
        """Create BSTNode"""
        return self.data
    def set_data(self, data):
        """Create BSTNode​"""
        self.data = data
    def get_left(self):
        """Create BSTNode"""
        return self.left
    def set_left(self, left):
        """Create BSTNode​"""
        self.left = left
    def get_right(self):
        """Create BSTNode"""
        return self.right
    def set_right(self, right):
        """Create BSTNode​"""
        self.right = right
class BST:
    """Create BSTNode​​"""
    def __init__(self):
        """Create BSTNode"""
        self.root = None
        self.pnew = None
        self.maxvalue = 0
        self.minvalue = 0
        self.text = ""
    def get_root(self):
        """Create BSTNode"""
        return self.root
    def set_root(self, root):
        """Create BSTNode"""
        self.root = root
    def insert(self, data):
        """Create BSTNode"""
        self.pnew = BSTNode(data)
        self.text += "*" + str(data)
        if self.is_empty():
            self.set_root(self.pnew)
            self.maxvalue = data
            self.minvalue = data
        else:
            self.last_node(self.root)
    def last_node(self, root):
        """Create BSTNode"""
        if root != None:
            if root.data > self.pnew.data:
                root.left = self.last_node(root.left)
                return root
            elif root.data < self.pnew.data:
                root.right = self.last_node(root.right)
                return root
        elif root == None:
            return self.pnew
    def is_empty(self):
        """Create BSTNode"""
        if self.root == None:
            return True
        else:
            return False
    def delete(self, data):
        """Create BSTNode"""
        text = self.text.split("*")
        self.text = ""
        self.root = None
        che = True
        for txt in text:
            if txt != "" and txt != str(data):
                self.insert(int(txt))
            if txt == str(data):
                che = False
        if che:
            print("Delete Error, {0} is not found in Binary Search Tree.".format(data))
    def preorder(self, root):
        """Create BSTNode​"""
        if root != None:
            print("->", root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def inorder(self, root):
        """Create BSTNode"""
        if root != None:
            self.inorder(root.left)
            print("->", root.data, end=" ")
            self.inorder(root.right)
    def postorder(self, root):
        """Create BSTNode​"""
        if root != None:
            self.postorder(root.left)
            self.postorder(root.right)
            print("->", root.data, end=" ")
    def traverse(self):
        """Create BSTNode​"""
        if self.is_empty():
            return print("This is an empty binary search tree.")
        print('Preorder: ', end='')
        self.preorder(self.root)
        print("")
        print('Inorder: ', end='')
        self.inorder(self.root)
        print("")
        print('Postorder: ', end='')
        self.postorder(self.root)
    def find_min(self):
        """Create BSTNode​"""
        self.calculate(self.root)
        return self.minvalue
    def find_max(self):
        """Create BSTNode​"""
        self.calculate(self.root)
        return self.maxvalue
    def calculate(self, root):
        """Create BSTNode​"""
        if root != None:
            self.calculate(root.left)
            self.calculate(root.right)
            if self.minvalue > root.data:
                self.minvalue = root.data
            elif self.maxvalue < root.data:
                self.maxvalue = root.data
def main():
    """Data Structures and Algorithms"""
    my_bst = BST()
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            my_bst.delete(int(data))
        else:
            print("Invalid Condition")
    my_bst.traverse()
main()
