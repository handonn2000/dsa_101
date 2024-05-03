from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None) -> None:
        self.val = value
        self.left = left
        self.right = right
    def __str__(self) -> str:
        return str(self.value)

class BinaryTree:
    def __init__(self, value) -> None:
        self.root = TreeNode(value)

    # DFS: left -> root -> right
    def inorder(self):
        display = []
        def traverse(current_node):
            if current_node is None:
                return 
            traverse(current_node.left)
            display.append(current_node.val)
            traverse(current_node.right)

        traverse(self.root)
        return " -> ".join(map(str, display))

    # DFS: left -> right -> root
    def postorder(self):
        display = []

        def traverse(current_node):
            if current_node is None:
                return
            
            traverse(current_node.left)
            traverse(current_node.right)
            display.append(current_node.val)
            
        traverse(self.root)
        return ' -> '.join(map(str, display))

    # DFS: root -> left -> right
    def preorder(self):
        display = []
        
        def traverse(current_node):
            if current_node is None:
                return
            
            display.append(current_node.val)
            traverse(current_node.left)
            traverse(current_node.right)

        traverse(self.root)
        return ' -> '.join(map(str, display))

    def bfs(self):
        display = []
        queue = deque()

        queue.append(self.root)
        while queue:
            current_node = queue.popleft()
            display.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return ' -> '.join(map(str, display))


print("-"*5 + "DFS" + "-"*5)
binaryTree = BinaryTree(1)
binaryTree.root.left = TreeNode(12, TreeNode(5), TreeNode(6))
binaryTree.root.right = TreeNode(9)
print("Inorder: " + binaryTree.inorder())
print("Postorder: " + binaryTree.postorder())
print("Preorder: " + binaryTree.preorder())

print()
print("-"*5 + "BFS" + "-"*5)
binaryTree = BinaryTree('F')
binaryTree.root.left = TreeNode('B',
    TreeNode('A'), 
    TreeNode('D', 
        TreeNode('C'),
        TreeNode('E'))
    )
binaryTree.root.right = TreeNode('G',
                            TreeNode('I'), 
                            TreeNode('H')
                        )
print("BFS: " + binaryTree.bfs())
