class LLRedBlackTree:

    class Node:
        def __init__(self, key, red=True):
            self.key = key
            self.red = red  # Colour of link to its parent
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        self.size = 1

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None:
            return root
        if root.key == key:
            return root
        else:
            if root.key < key:
                return self._search(root.right, key)
            else:
                return self._search(root.left, key)

    def insert(self, key):
        self.root = self._insert(self.root, key)
        self.root.red = False

    # def _insert(self, root, key):
    #     if root is None:
    #         root = self.Node(key)
    #     else:
    #         if not root.red:
    #             if key < root.key:
    #                     root.left = self._insert(root.left, key)
    #                     if not root.left.red:
    #                         root.red = True
    #             else:
    #                     root.right = self._insert(root.right, key)
    #                     if not root.right.red:
    #                         y = root.right
    #                         y.red = True
    #                         root.right = y.left
    #                         y.left = root
    #                         root = y
    #         else:
    #             if key < root.left.key:
    #                 root.left.left = self._insert(root.left.left, key)
    #                 if not root.left.left.red:
    #                     root.red = False
    #                     left = root.left
    #                     root.left = left.right
    #                     left.right = root
    #                     root = left
    #             elif key < root.key:
    #                 root.left.right = self._insert(root.left.right, key)
    #                 if not root.left.right.red:
    #                     root.red = False
    #                     middle = root.left.right
    #                     root.left.right = middle.left
    #                     middle.left = root.left
    #                     root.left = middle.right
    #                     middle.right = root
    #                     root = middle
    #             else:
    #                 root.right = self._insert(root.right, key)
    #                 if not root.right.red:
    #                     root.red = False
    #     return root

    def _insert(self, root, key):
        if root is None:
            root = self.Node(key)
        else:
            if key < root.key:
                root.left = self._insert(root.left, key)
            else:
                root.right = self._insert(root.right, key)
            if not self._is_red(root.left) and self._is_red(root.right):
                root = self._left_rotate(root)
            if self._is_red(root.left) and self._is_red(root.left.left):
                root = self._right_rotate(root)
            if self._is_red(root.right) and self._is_red(root.left):
                root = self._flip_colors(root)
        return root

    @staticmethod
    def _is_red(root):
        return False if root is None else root.red

    @staticmethod
    def _flip_colors(root):
        root.left.red = False
        root.right.red = False
        root.red = True
        return root

    @staticmethod
    def _left_rotate(root):
        y = root.right
        y.red = root.red  # The colour of the link to the root parent is copied
        root.right = y.left
        root.red = True  # this new link is a red link. Important
        y.left = root
        return y

    @staticmethod
    def _right_rotate(root):
        # assert root.left.red
        x = root.left
        x.red = root.red  # The colour of the link to the root parent is copied
        root.left = x.right
        root.red = True  # this new link is a red link. Important
        x.right = root
        return x

    def delete(self, key):
        self.root = self._delete(self.root, key)

    @staticmethod
    def _delete(root, key):
        if root is None:
            return
        else:
            if root.key > key:
                root.left = LLRedBlackTree._delete(root.left, key)
            elif root.key < key:
                root.right = LLRedBlackTree._delete(root.right, key)
            else:
                pass
            return root

    def find_min(self):
        pass

    def find_max(self):
        pass

    def contains(self, key):
        return self._search(self.root, key) is not None

    def print_level_order(self):
        self._print_level_order(self.root)
        print()

    def print_in_order(self):
        self._print_in_order(self.root)
        print()

    @staticmethod
    def _print_in_order(root):  # sorting
        if root is None:
            return
        else:
            if root.left is not None:
                LLRedBlackTree._print_in_order(root.left)
            print(root.key, end=" ")
            if root.right is not None:
                LLRedBlackTree._print_in_order(root.right)

    @staticmethod
    def _print_level_order(root):
        if root is None:
            return
        else:
            tree = list()
            tree.append(root)
            while len(tree) > 0:
                # assert not LLRedBlackTree._is_red(tree[0].right)
                if not LLRedBlackTree._is_red(tree[0].left):
                    if tree[0].left is not None:
                        tree.append(tree[0].left)
                    if tree[0].right is not None:
                        tree.append(tree[0].right)
                    print(tree[0].key, end=" ")
                else:
                    if tree[0].left.left is not None:
                        tree.append(tree[0].left.left)
                    if tree[0].left.right is not None:
                        tree.append(tree[0].left.right)
                    if tree[0].right is not None:
                        tree.append(tree[0].right)
                    print((tree[0].left.key, tree[0].key), end=" ")
                tree.remove(tree[0])

if __name__ == '__main__':
    # 1. Insertion at empty root
    redblack1 = LLRedBlackTree()
    redblack1.insert(24)
    redblack1.print_level_order()
    # 2. Right insertion at 2 node
    redblack1.insert(32)
    redblack1.print_level_order()
    # 3. Left insertion at 2 node
    redblack2 = LLRedBlackTree()
    redblack2.insert(24)
    redblack2.insert(12)
    redblack2.print_level_order()
    # 4. Left insertion at 3 node
    redblack1.insert(3)
    redblack1.print_level_order()
    # 5. Middle insertion at 3 node
    redblack2.insert(18)
    redblack2.print_level_order()
    # 6. Right insertion at 3 node
    redblack3 = LLRedBlackTree()
    redblack3.insert(36)
    redblack3.insert(24)
    redblack3.insert(72)
    redblack3.print_level_order()
    # 7. All insertions with only 2 node as ancestors
    redblack3.insert(96)
    redblack3.print_level_order()
    redblack2.insert(22)
    redblack2.print_level_order()
    redblack3.insert(52)
    redblack3.print_level_order()
    # 7. All insertions with both 2 node and 3 node as ancestors
    redblack3.insert(28)
    redblack3.insert(46)
    redblack3.insert(74)
    redblack3.print_level_order()
    redblack3.insert(11)
    redblack3.print_level_order()
    redblack3.print_in_order()
    # 8. Random insertions
    redblack4 = LLRedBlackTree()
    import random
    random.seed(1)
    redblack4.insert(random.randint(0, 1000))
    redblack4.insert(random.randint(0, 1000))
    redblack4.insert(random.randint(0, 1000))
    redblack4.insert(random.randint(0, 1000))
    redblack4.insert(random.randint(0, 1000))
    redblack4.insert(random.randint(0, 1000))
    redblack4.insert(random.randint(0, 1000))
    redblack4.insert(random.randint(0, 1000))
    redblack4.insert(random.randint(0, 1000))
    redblack4.insert(random.randint(0, 1000))
    redblack4.insert(random.randint(0, 1000))
    redblack4.insert(random.randint(0, 1000))
    redblack4.insert(random.randint(0, 1000))
    redblack4.print_level_order()
    redblack4.print_in_order()
    print(redblack4.search(483).key)
'''
24
(24, 32)
(12, 24)
24 3 32
18 12 24
36 24 72
36 24 (72, 96)
18 12 (22, 24)
(36, 72) 24 52 96
(36, 72) (24, 28) (46, 52) (74, 96)
36 24 72 11 28 (46, 52) (74, 96)
11 24 28 36 46 52 72 74 96
582 (137, 460) (779, 821) (64, 120) 261 (483, 507) 667 782 867
64 120 137 261 460 483 507 582 667 779 782 821 867
483
'''