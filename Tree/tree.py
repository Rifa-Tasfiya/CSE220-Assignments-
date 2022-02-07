class myTreeNode:
    def __init__(self, elem, left, right, parent):
        self.parent = parent
        self.left = left
        self.right = right
        self.elem = elem


class myBinaryTree:
    def __init__(self, arr):
        self.arr = arr
        self.root = self.build_tree(arr, 1)

    def build_tree(self, arr, i):
        size = len(arr)
        if i < 0 or i >= size or arr[i] is None:
            return None
        else:
            temp_root = myTreeNode(arr[i], None, None, None)
            temp_root.left = self.build_tree(arr, 2 * i)
            temp_root.right = self.build_tree(arr, 2 * i + 1)
            if temp_root.left:
                temp_root.left.parent = temp_root
            if temp_root.right:
                temp_root.right.parent = temp_root
            return temp_root

    def find_maximum(self, left, right):  ##### TASK-1
        if right > left:
            return right
        return left

    def calculate_height(self, root):
        if root is None:
            return -1
        return 1 + self.find_maximum(self.calculate_height(root.left), self.calculate_height(root.right))

    def calculate_level(self, given_node):  ##### TASK-2
        if given_node.parent:
            return 1 + self.calculate_level(given_node.parent)
        return 1

    def pre_order_traversal(self, root):  ###### TASK-3
        if root is None:
            return
        print(root.elem, end=" ")
        self.pre_order_traversal(root.left)
        self.pre_order_traversal(root.right)

    def in_order_traversal(self, root):  #### TASK-4
        if root is None:
            return
        self.in_order_traversal(root.left)
        print(root.elem, end=" ")
        self.in_order_traversal(root.right)

    def post_order_traversal(self, root):  #### TASK-5
        if root is None:
            return
        self.post_order_traversal(root.left)
        self.post_order_traversal(root.right)
        print(root.elem, end=" ")

    def is_exactly_same(self, root_1, root_2):  #### TASK-6
        if root_1 is None and root_2 is None:
            return True
        elif root_1 and root_2:
            if root_1.elem != root_2.elem:
                return False
            else:
                return (self.is_exactly_same(root_1.left, root_2.left)
                        and self.is_exactly_same(root_1.right, root_2.right))
        else:
            return False

    def get_copy_tree(self, root):  #### TASK-7
        if root is None:
            return None
        else:
            new_root = myTreeNode(root.elem, None, None, None)
            if root.left:
                new_root.left = self.get_copy_tree(root.left)
            if root.right:
                new_root.right = self.get_copy_tree(root.right)
            return new_root

    def show_copy_tree(self, root):
        print("None", end=" ")
        new_root = self.get_copy_tree(root)
        height = self.calculate_height(new_root)
        for i in range(1, height + 2):
            self.show_current_level(new_root, i)

    def show_current_level(self, new_root, level_no):
        if new_root is None:
            return
        if level_no == 1:
            print(new_root.elem, end=" ")
        elif level_no > 1:
            if (new_root.left == None):
                print("None", end=" ")
            if (new_root.right == None):
                print("None", end=" ")
            self.show_current_level(new_root.left, level_no - 1)
            self.show_current_level(new_root.right, level_no - 1)


# ===================================== Tester Code ==================================================================
arr_1 = [None, 10, 5, 7, 17, 9, None, 28]
arr_2 = [None, 10, 5, 7, 17, 9, None, 28]
tree_1 = myBinaryTree(arr_1)
tree_2 = myBinaryTree(arr_2)
# Task -> 1 -------the height of a tree.
print("-------------------------------// Task -> 1 //---------------------------------------------------------------")
print("The height of the given tree: " + str(tree_1.calculate_height(tree_1.root)))  ## Should print: 2
# Task -> 2 -------the level of a Node in a tree
print("\n-------------------------------// Task -> 2 //---------------------------------------------------------------")
print("The level of the given node is " + str(tree_1.calculate_level(tree_1.root)))  ## Should print: 1
# Task -> 3 -------Print elements of all the Nodes of a tree using Pre-order Traversal
print("\n-------------------------------// Task -> 3 //---------------------------------------------------------------")
print("All nodes of the tree according to Pre-order Traversal ----> ")
tree_1.pre_order_traversal(tree_1.root)  ## Should print: 10 5 17 9 7 28
# Task -> 4 -------Print elements of all the Nodes of a tree using In-order Traversal
print("\n-------------------------------// Task -> 4 //---------------------------------------------------------------")
print("All nodes of the tree according to In-order Traversal ----> ")
tree_1.in_order_traversal(tree_1.root)  ## Should print: 17 5 9 10 7 28
# Task -> 5 -------Print elements of all the Nodes of a tree using Post-order Traversal
print("\n-------------------------------// Task -> 5 //---------------------------------------------------------------")
print("All nodes of the tree according to Post-order Traversal ----> ")
tree_1.post_order_traversal(tree_1.root)  ## Should print: 17 9 5 28 7 10
# Task -> 6 -------evaluate whether two trees are exactly same or not
print("\n-------------------------------// Task -> 6 //---------------------------------------------------------------")
if tree_1.is_exactly_same(tree_1.root, tree_2.root):  ## Should print: Two trees are exactly same.
    print("Two trees are exactly same.")
else:
    print("Two trees are NOT exactly same.")
# Task -> 7 -------return a copy (new tree) of a given tree.
print("\n-------------------------------// Task -> 7 //---------------------------------------------------------------")
print("The copy of the given tree: ")
tree_1.show_copy_tree(tree_1.root)  ## Should print: None 10 5 7 17 9 None 28
