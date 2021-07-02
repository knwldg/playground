from custom_collections import LinkedList, Node, Stack, Tree, TreeNode

if __name__ == '__main__':
    tree = Tree()

    tree.root = TreeNode(1)
    tree.root.left = TreeNode(2)
    tree.root.left.left = TreeNode(4)
    tree.root.left.right = TreeNode(5)
    tree.root.right = TreeNode(3)
    tree.root.right.left = TreeNode(6)
    tree.root.right.right = TreeNode(7)

    res = tree.postorder_traversal_iterative()

    for i in res:
        print(i)
