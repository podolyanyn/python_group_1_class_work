# # myTree = [3,
# #             [5,
# #                 [8,[],[]],
# #                 [6, [], []]
# #              ],
# #             [4, [],[]]
# #           ]
#
#
# def binary_tree(r):
#     return [r, [], []]
# def insertLeft(root,newBranch):
#     t = root.pop(1)
#     if len(t) > 1:
#         root.insert(1,[newBranch,t,[]])
#     else:
#         root.insert(1,[newBranch, [], []])
#     return root
# def insertRight(root,newBranch):
#     t = root.pop(2)
#     if len(t) > 1:
#         root.insert(2,[newBranch,[],t])
#     else:
#         root.insert(2,[newBranch, [], []])
#     return root
#
# def get_root_value(root):
#     return root[0]
#
# def get_leftChild(root):
#     return root[1]
#
# def get_rightChild(root):
#     return root[2]
#
#
#
# my_tree = binary_tree(3)
# insertLeft(my_tree,5)
# print(my_tree)
# insertLeft(my_tree,10)
# print(my_tree)
#
# insertRight(my_tree,4)
# print(my_tree)
# print(get_rightChild(my_tree))
#
# print(get_leftChild(my_tree))
# print(get_leftChild(get_leftChild(my_tree)))
# insertRight(get_leftChild(get_leftChild(my_tree)), 23)
# print(my_tree)


class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def pre_order(self) -> None:
        print(self.key, ' -> ', end ='')
        if self.leftChild:
            self.leftChild.pre_order()
        if self.rightChild:
            self.rightChild.pre_order()

    def post_order(self) -> None:
        if self.leftChild:
            self.leftChild.post_order()
        if self.rightChild:
            self.rightChild.post_order()
        # print(self.key)
        print(self.key, ' -> ', end='')

    def in_order(self) -> None:
        if self.leftChild:
            self.leftChild.in_order()
        # print(self.get_root_val())
        print(self.key, ' -> ', end='')
        if self.rightChild:
            self.rightChild.in_order()

#
# r = BinaryTree('a')
# print(r.getRootVal())
# print(r.getLeftChild())
# r.insertLeft('b')
# print(r.getLeftChild())
# print(r.getLeftChild().getRootVal())
# r.insertRight('c')
# print(r.getRightChild())
# print(r.getRightChild().getRootVal())
# r.getRightChild().setRootVal('hello')
# print(r.getRightChild().getRootVal())

root = BinaryTree(3)
print(root.getRootVal())
root.insertLeft(5)
print(root.getLeftChild().getRootVal())
root.insertLeft(10)
print(root.getLeftChild().getRootVal())
root.getLeftChild().getLeftChild().insertRight(23)
print(root.getLeftChild().getLeftChild().getRightChild().getRootVal())
root.insertRight(4)
print(root.getRightChild().getRootVal())
root.pre_order()
print()
root.post_order()
print()
root.in_order()
