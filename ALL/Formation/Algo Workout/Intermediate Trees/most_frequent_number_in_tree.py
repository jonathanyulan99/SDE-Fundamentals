'''
Q:
Prompt

Given a binary tree, return the most frequent value in the tree.
Examples

Input:
          1 
        /    \
      2       3
     / \      / \
   2   3   2   2
Output: 2
'''
class Node(object):
      def __init__(self,value=0,left=None,right=None):
            self.val = value 
            self.left = left 
            self.right = right 
            
def find_most_frequent_value(root):
    freq = {}
    max_freq = 0
    most_freq_val = None

    def dfs(node):
        nonlocal max_freq, most_freq_val

        if node is None:
            return

        freq[node.val] = freq.get(node.val, 0) + 1
        if freq[node.val] > max_freq:
            max_freq = freq[node.val]
            most_freq_val = node.val

        dfs(node.left)
        dfs(node.right)

    dfs(root)

    return most_freq_val