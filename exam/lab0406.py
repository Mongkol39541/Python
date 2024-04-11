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
        """Create BSTNode"""
        self.right = right
class BST:
    """Create BSTNode"""
    def __init__(self):
        """Create BSTNode"""
        self.root = None
        self.pnew = None
        self.maxvalue = 0
        self.minvalue = 0
        self.text = ""
        self.text2 = ""
        self.keep = 0
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
        if str(data) not in self.text:
            return print("Delete Error, {0} is not found in Binary Search Tree.".format(data))
        self.text2 = ""
        self.keep = 0
        keep3 = self.root.data
        self.find_value(self.root, data)
        keep1 = self.keep
        keep2 = 0
        text = self.text.split("*")
        self.root = None
        self.text = ""
        text.remove("")
        copytext = text.copy()
        che = True
        for txt in copytext:
            if txt != str(data):
                self.insert(int(txt))
                if che:
                    keep2 = txt
            else:
                text.remove(txt)
                che = False
        self.text = ""
        for txt in text:
            self.text += "*" + txt
        if self.keep != 0:
            self.deleteall(keep1, keep2, keep3)
    def deleteall(self, keep1, keep2, keep3):
        """Create BSTNode"""
        text2 = self.text2.split("*")
        text2.remove("")
        val_max = 0
        for num in text2:
            if num == str(keep1):
                break
            if val_max < int(num):
                val_max = int(num)
        text2 = self.text.split("*")
        text2.remove("")
        text = ""
        if keep1 == keep3:
            loop = 0
            for num in text2:
                if loop == len(text2) - 1:
                    text += "*" + str(val_max)
                loop += 1
        for num in text2:
            if num == str(val_max):
                pass
            else:
                text += "*" + num
            if num == str(keep2):
                text += "*" + str(val_max)
        text = text.split("*")
        text.remove("")
        self.root = None
        self.text = ""
        for txt in text:
            self.insert(int(txt))
    def find_value(self, root, data):
        """Create BSTNode"""
        if root != None:
            self.find_value(root.left, data)
            self.text2 += "*" + str(root.data)
            self.find_value(root.right, data)
            if root.data == data and root.left != None and root.right != None:
                self.keep = root.data
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
