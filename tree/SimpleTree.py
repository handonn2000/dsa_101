class TreeNode:
    def __init__(self, key, value, children=[]) -> None:
        self.key = key
        self.value = value
        self.children = children
    def __str__(self) -> str:
        return str(self.key) + ": " + str(self.value)

class Tree:
    def __init__(self, key, value) -> None:
        self.root = TreeNode(key, value)

    def __str__(self) -> str:
        display = str(self.root)
        current_node = self.root
        for child in current_node.children:
            display += " -> " + str(child)
        return display
    


tree = Tree(1, "a")
subTree1 = TreeNode(2, "b")
subTree2 = TreeNode(3, "c")
subTree3 = TreeNode(4, "d")
subTree4 = TreeNode(5, "e")
subTree1.children = [subTree3, subTree4]
tree.root.children = [subTree1, subTree2]
print(tree.root)
print(tree.root.children[0])
print(" " + str(tree.root.children[0].children[0]))
print(" " + str(tree.root.children[0].children[1]))
print(tree.root.children[1])