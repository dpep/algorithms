#!/usr/bin/env python

'''
Binary Search Tree

add, search, and remove some values...
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

    def __eq__(self, other):
        return other and self.val.__eq__(other.val)

    def __lt__(self, other):
        return other and self.val.__lt__(other.val)


class Tree:
    def __init__(self):
        self.root = None


    def add(self, val):
        '''
        add a new node to the tree
        '''
        node = Node(val)

        if self.root is None:
            self.root = node
        else:
            root = self.root
            while True:
                if node < root:
                    if root.left:
                        root = root.left
                    else:
                        root.left = node
                        break
                else:
                    if root.right:
                        root = root.right
                    else:
                        root.right = node
                        break

    def __lshift__(self, val):
        self.add(val)


    def remove(self, val):
        '''
        remove specified value from the tree
        '''
        def next(root):
            if root.left:
                return next(root.left)
            return root

        def rm(parent, root, node):
            if root is None:
                raise ValueError

            if node == root:
                if root.right:
                    # replace with successor
                    succ = next(root.right)
                    root.val = succ.val
                    rm(root, root.right, succ)
                elif root.left:
                    # node only has a left child, replace
                    root.val = root.left.val
                    root.right = root.left.right
                    root.left = root.left.left
                else:
                    # leaf node, just unlink
                    if parent is None:
                        self.root = None
                    elif parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None

            # else recurse to find node
            elif node < root:
                rm(root, root.left, node)
            else:
                rm(root, root.right, node)

        rm(None, self.root, Node(val))


    def __iter__(self):
        def nodes(root):
            if root:
                for node in nodes(root.left):
                    yield node

                yield root

                for node in nodes(root.right):
                    yield node

        for node in nodes(self.root):
            yield node.val


    def __contains__(self, val):
        def contains(root, node):
            if root is None:
                return False

            if node == root:
                return True

            if node < root:
                return contains(root.left, node)
            else:
                return contains(root.right, node)

        return contains(self.root, Node(val))


    def __len__(self):
        count = 0
        for i in self:
            count +=1
        return count



# testing
vals = [ 5, 3, 6, 2, 8, 1 ]

tree = Tree()
for v in vals:
    tree << v

assert sorted(vals) == list(tree)
assert 5 in tree
for v in vals:
    assert v in tree
assert 0 not in tree
assert len(vals) == len(tree)

# test deletions
remaining = set(vals)
assert set(remaining) == set(tree)
assert sorted(remaining) == list(tree)

tree.remove(2)
remaining.remove(2)
assert sorted(remaining) == list(tree)
assert len(remaining) == len(tree)

tree.remove(5)
remaining.remove(5)
assert sorted(remaining) == list(tree)
assert len(remaining) == len(tree)
