class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

    def __repr__(self):
        return str(self.val)


class LinkedList:
    def __init__(self):
        self.start_node = None

    def __len__(self):
        if self.start_node is None:
            return 0

        counter = 1
        curr = self.start_node
        while curr.next is not None:
            counter += 1
            curr = curr.next

        return counter

    def __getitem__(self, index):
        if self.start_node is None:
            raise IndexError

        if index == 0:
            return self.start_node

        counter = 0
        curr = self.start_node

        while counter < index:
            if curr.next is not None:
                counter += 1
                curr = curr.next
            else:
                raise IndexError

        return curr

    def __setitem__(self, key, value):
        if key > len(self) - 1:
            raise IndexError

        counter = 0
        curr = self.start_node

        while counter < key:
            counter += 1
            curr = curr.next

        curr.val = value

    def __contains__(self, item):
        if self.start_node is None:
            return False
        if self.start_node.val == item:
            return True

        curr = self.start_node

        while curr.next is not None:
            curr = curr.next

            if curr.val == item:
                return True

        return False

    def __iter__(self):
        if self.start_node is None:
            return None  # am i supposed to return None here?

        curr = self.start_node
        yield curr

        while curr.next is not None:
            curr = curr.next
            yield curr

    def append(self, value):
        if self.start_node is None:
            self.start_node = Node(value)
        else:
            curr = self.start_node

            while curr.next is not None:
                curr = curr.next
            curr.next = Node(value)

    def remove(self, value):
        if self.start_node is None:
            raise IndexError

        if self.start_node.val == value:
            self.start_node = self.start_node.next

        curr = self.start_node

        while curr.next is not None:
            prev = curr
            curr = curr.next

            if curr.val == value:
                prev.next = curr.next

    def remove_at(self, index):
        if self.start_node is None:
            raise IndexError

        if index > len(self) - 1:
            raise IndexError

        if self.start_node.next is None:
            self.start_node = None
            return

        if index == 0:
            self.start_node = self.start_node.next
            return

        counter = 0
        curr = self.start_node

        while curr.next is not None:
            prev = curr
            curr = curr.next
            counter += 1

            if counter == index:
                prev.next = curr.next
                return


class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def __len__(self):
        return len(self.linked_list)

    def __iter__(self):
        if self.linked_list.start_node is None:
            return None  # same issue as above

        curr = self.linked_list.start_node
        yield curr.val

        while curr.next is not None:
            curr = curr.next
            yield curr.val

    def __repr__(self):
        return f"{[i for i in self.linked_list]}"

    def push(self, value):
        self.linked_list.append(value)

    def pop(self):
        if self.linked_list.start_node is None:
            raise IndexError

        index = len(self.linked_list) - 1
        value = self.linked_list[index]
        self.linked_list.remove_at(index)
        return value.val

    def peek(self):
        return self.linked_list[len(self.linked_list) - 1].val

    def reverse(self):
        stack = Stack()
        while len(self.linked_list) > 0:
            stack.push(self.pop())
        self.linked_list = stack.linked_list
        return self


class TreeNode:
    def __init__(self, value=0, left=None, right=None):  # better initialization style
        self.val = value
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Tree:
    def __init__(self, value=0):
        self.root = TreeNode(value)

    def traverse_preorder(self):
        results = []

        def recurse(node):
            if node:
                results.append(node.val)
                recurse(node.left)
                recurse(node.right)

        recurse(self.root)
        return results

    def traverse_inorder(self):
        results = []

        def recurse(node):
            if node:
                recurse(node.left)
                results.append(node.val)
                recurse(node.right)

        recurse(self.root)
        return results

    def traverse_postorder(self):
        results = []

        def recurse(node):
            if node:
                recurse(node.left)
                recurse(node.right)
                results.append(node.val)

        recurse(self.root)
        return results

    def postorder_traversal_iterative(self):  # i know this is usually done recursively, but I dislike recursion
        stack = Stack()
        results = Stack()

        stack.push(self.root)

        while len(stack) > 0:
            curr = stack.pop()
            results.push(curr.val)

            if curr.left is not None:
                stack.push(curr.left)

            if curr.right is not None:
                stack.push(curr.right)

        return results.reverse()
