from DataStructures.custom_collections import Tree, TreeNode


def inorder_traversal(root) -> [int]:
    results = []

    def recurse(node):
        if node:
            recurse(node.left)
            results.append(node.val)
            recurse(node.right)

    recurse(root)
    return results


if __name__ == '__main__':
    tree = Tree()
    tree.root = TreeNode(1)
    tree.root.right = TreeNode(3)
    tree.root.left = TreeNode(2)
    tree.root.left = TreeNode(2)
    tree.root.left.left = TreeNode(4)
    tree.root.left.right = TreeNode(5)

    print(inorder_traversal(tree.root))
