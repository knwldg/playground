from DataStructures.custom_collections import Tree, TreeNode


def inorder_traversal(root) -> [int]:
    results = []

    def recurse(node):
        if node:
            recurse(node)
            results.append(node.val)
            recurse(node)
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
