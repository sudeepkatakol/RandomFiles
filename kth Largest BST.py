class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def insert(root, key):
    if root is None:
        root = Node(key)
    else:
        if root.key >= key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def _get_inorder_in_list(root):
    if root is None:
        return
    else:
        global count, k, key
        if root.left is not None:
            _get_inorder_in_list(root.left)
        count += 1
        if count == k:
            key = root.key
            return
        if root.right is not None:
            return _get_inorder_in_list(root.right)


# find_min and find_max also return references to the minimum here
def find_min(root):
    if root is None:
        return None
    elif root.left is None:
        return root
    else:
        return find_min(root.left)


def find_max(root):
    if root is None:
        return None
    elif root.right is None:
        return root
    else:
        return find_max(root.right)



# Replace it by the max of the left subtree or the min of the right subtree
def delete(root, key):
    if root is None:
        return
    else:
        if root.key == key:
            if root.right is None:
                if root.left is None:
                    root = None
                else:
                    root.key = find_max(root.left).key
                    root.left = delete(root.left, root.key)
            else:
                root.key = find_min(root.right).key
                root.right = delete(root.right, root.key)
            return root
        else:
            if root.key >= key:
                root.left = delete(root.left, key)
            else:
                root.right = delete(root.right, key)
            return root


def print_level_order(root):
    if root is None:
        return
    else:
        tree = list()
        tree.append(root)
        while len(tree) > 0:
            if tree[0].left is not None:
                tree.append(tree[0].left)
            if tree[0].right is not None:
                tree.append(tree[0].right)
            print(tree[0].key, end=" ")
            tree.remove(tree[0])

if __name__ == "__main__":
    key = 0
    count = 0
    n, k = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))
    k = n - k + 1
    root = None
    for x in arr:
        root = insert(root, x)
    _get_inorder_in_list(root)
    root = delete(root, key)
    print_level_order(root)