'''
Tree
'''

from treelib import Node, Tree
from utils import GetTreeLevel
import pickle


class TreeNode:
    '''
    "TreeNode" class defines tree node structure.
    Each class instance (node) is composed  the following atributes:
        - status: status of the subtest ("ok" or "not ok");
        - comment: comment after each test;
        - output: concatenates "status" and "comment" attributes. 
    '''
    def __init__(self, status = "", comment = ""):
        self.status = status
        self.comment = comment
        self.output = str(status) + " " + str(comment)


class TreeManagement:

    '''
    "TreeManagement" class defines trees used to store tests data.
    Each class instance is composed by the following attributes:
        - nodeList: auxiliar array used to associate child nodes to its parent node;
        - 
        - subTree: auxiliar tree used to store subtests data, which is later merged into the "mainTree"
        - mainTree: tree used to store test data
        - nodeRoot: used to intialize "mainTree" root
    '''

    def __init__(self):
        self.nodeList = [None] * 100
        self.node = None
        self.subTree = Tree()
        self.mainTree = Tree()
        self.nodeRoot = self.mainTree.create_node(tag = "Root", identifier= "root", data=TreeNode("root", "root"))

    def CreateTestOkNode(self, value):
        '''
        This method creates a "ok" status test node and adds it to the tree
        Arguments:
            - value: node identification
        '''
        if self.subTree != None:
            self.node = self.mainTree.create_node(value, value, parent= self.nodeRoot, data = TreeNode("OK", ""))
            self.mainTree.merge(value, self.subTree)
        else:
            self.mainTree.create_node(value, value, parent= self.nodeRoot, data = TreeNode("OK", ""))

    def CreateSubtestOkNode(self, value):
        '''
        This method creates a "ok" status subtest node and adds it to the tree
        Arguments:
            - value: node identification
        '''
        n = GetTreeLevel(value)
        if n == 1:
            if self.subTree != None:
                self.node = self.subTree.get_node("aux")
            if self.node == None:
                self.subTree = Tree()
                self.nodeList[n-1] = self.subTree.create_node("aux", "aux", data = TreeNode("OK", ""))
        self.nodeList[n] = self.subTree.create_node(value, value, parent=self.nodeList[n-1], data = TreeNode("OK", ""))

    def CreateTestNotOkNode(self, value):
        '''
        This method creates a "not ok" status test node and adds it to the tree
        Arguments:
            - value: node identification
        '''
        if self.subTree != None:
            self.node = self.mainTree.create_node(value, value, parent= self.nodeRoot, data = TreeNode("OK", ""))
            self.mainTree.merge(value, self.subTree)
        else:
            self.mainTree.create_node(value, value, parent= self.nodeRoot, data = TreeNode("OK", ""))

    def CreateSubtestNotOkNode(self, value):
        '''
        This method creates a "not ok" status subtest node and adds it to the tree
        Arguments:
            - value: node identification
        '''
        n = GetTreeLevel(value)
        if n == 1:
            if self.subTree != None:
                self.node = self.subTree.get_node("aux")
            if self.node == None:
                self.subTree = Tree()
                self.nodeList[n-1] = self.subTree.create_node("aux", "aux", data = TreeNode("NOT OK", ""))
        self.nodeList[n] = self.subTree.create_node(value, value, parent=self.nodeList[n-1], data = TreeNode("NOT OK", ""))