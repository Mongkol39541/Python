# Decision Tree
# 31/10/2022
# Copyright (C) 2022

from treeplot import treeplot

class DecisionTree:
    def __init__(self, parent=[], node=[], branch=[]):
        self.parent = parent
        self.node = node
        self.branch = branch

    def show(self):
        treeplot(self.parent, vlabel=self.node, elabel=self.branch)

if __name__ == '__main__':
    parent = [0, 1, 1, 1, 2, 2, 4, 4]
    node = ['A1', 'A2', '+', 'A3', '-', '+', '-']
    branch = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7']
    tree = DecisionTree(parent, node, branch)
    tree.show()