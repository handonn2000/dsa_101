class BinaryTreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self, val) -> None:
        self.root = BinaryTreeNode(val)

    def inorder_traversal(self) -> None:
        display = []
        def traverse(node):
            if node is None:
                return

            traverse(node.left)
            display.append(node.val)
            traverse(node.right)
        traverse(self.root)
        
        print(display)

    def insert(self, val) -> None:
        new_node = BinaryTreeNode(val)
        def dfs(node):
            if node is None:
                return new_node
            
            if val > node.val:
                node.right = dfs(node.right)
            else:
                node.left = dfs(node.left)

            return node

        dfs(self.root)

    def search(self, val) -> bool:
        def dfs(node):
            if node is None:
                return False
            if node.val == val:
                return True
            
            search_left = dfs(node.left)
            search_right = dfs(node.right)
            return search_left or search_right

        res =  dfs(self.root)
        print(res)
        return res
    
    def find_min(self):
        node = self.root
        while node.left:
            node = node.left

        print(node.val)
        return node

    def find_max(self):
        node = self.root
        while node.right:
            node = node.right

        print(node.val)
        return node

    def find_node(self, val):
        def dfs(node):
            if node is None:
                return None
            if node.val == val:
                return node
            
            search_left = dfs(node.left)
            search_right = dfs(node.right)
            return search_left or search_right

        return dfs(self.root)
    
    def delete(self, val):
        def dfs(node, val):
            # Tree is empty
            if node is None:
                return node
            
            # Find the delete node
            if val > node.val:
                node.right = dfs(node.right, val)
            elif val < node.val:
                node.left = dfs(node.left, val)
            else: 
                # If the node have single childe
                if node.left is None or node.right is None:
                    temp = node.right or node.left
                    node = None
                    return temp
                
                # If node have 2 child, find min_value from the node
                temp = self.find_min(node)
                node.val = temp.val
                node.right = dfs(node.right, temp.val)

        dfs(self.root, val)
        self.inorder_traversal()


tree = BinarySearchTree(5)
tree.inorder_traversal()
tree.insert(4)
tree.insert(7)
tree.insert(3)
tree.insert(9)
tree.insert(11)
tree.inorder_traversal() # 3 4 5 7 9 11
tree.search(3) # True
tree.search(10) # False
tree.find_min() # 3
tree.find_max() # 11
tree.delete(4) # 3 5 7 9 11
tree.delete(3) # 5 7 9 11
tree.delete(7) # 5 9 11
