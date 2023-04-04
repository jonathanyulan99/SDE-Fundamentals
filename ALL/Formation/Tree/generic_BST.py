class TNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BST(object):
    def __init__(self, root):
        self.root = root

    def insert(self, value):
        return self._insert(self, self.root, value)

    def _insert(self, curr, value):
        if curr and curr.value < value:
            if curr.right:
                return self._insert(self, curr.right, value)
            else:
                curr.right = TNode(value)
        elif curr and curr.value > value:
            if curr.left:
                return self._insert(curr.left, value)
            else:
                curr.left = TNode(value)

    def search(self, searched):
        if self.root:
            found = self._search(self.root, searched)
            if found:
                return True
            else:
                return False
        else:
            return False

    def _search(self, curr, searched):
        if curr.value == searched:
            return True
        elif curr.value < searched:
            if curr.right:
                return self._search(curr.right, searched)
            else:
                return False
        elif curr.value > searched:
            if curr.left:
                return self._searched(curr.left, searched)
            else:
                return False

    def in_order_print(self):
        if self.root:
            self._in_order_print(self.root)
            print('Done')
        else:
            return None

    def _in_order_print(self, curr):
        if curr:
            self._in_order_print(curr.left)
            print(curr.value, end='->')
            self._in_order_print(curr.right)


leftLeft, leftRight = TNode(2), TNode(7)
rightLeft, rightRight = TNode(12), TNode(17)
left = TNode(5, leftLeft, leftRight)
right = TNode(15, rightLeft, rightRight)
# TNode(10, left, right)
rightLeft.right = TNode(13)
root = BST(TNode(10, left, right))
root.in_order_print()
