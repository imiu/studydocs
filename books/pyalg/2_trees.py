#!/usr/bin/env python


# Simpiest binary tree
class BinaryTree:
    def __init__(self, left, right):
        self.left = left
        self.right = right


#      o
#    /   \
#   o     o
#  / \   / \
# a   b c   d
#
#
#
t = BinaryTree(BinaryTree("a", "b"), BinaryTree("c", "d"))
print t.right.left


# Unrestricted tree
class Tree:
    def __init__(self, kids, next=None):
        self.val = self.kids = kids
        self.next = next

#    _o_
#  / / \ \
# a b   c d
#
#
t = Tree(Tree("a", Tree("b", Tree("c", Tree("d")))))
print t.kids.next.next.next.val
