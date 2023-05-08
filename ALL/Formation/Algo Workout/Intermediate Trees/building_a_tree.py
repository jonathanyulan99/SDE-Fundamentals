class TreeNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []

def build_tree(edges):
    # Create a list to store nodes
    nodes = [None] * len(edges)

    # Iterate through the edges and add them to the list
    for i, children in enumerate(edges):
        nodes[i] = TreeNode(i)
        for child in children:
            if child is not None:
                nodes[i].children.append(nodes[child])

    # Return the root node of the tree
    return nodes[0]

print(build_tree([[None, 1], [None, 2], [None, 3], []]))

