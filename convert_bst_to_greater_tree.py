'''
https://leetcode.com/problems/convert-bst-to-greater-tree/
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.
Example:
Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13
Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
'''

class Solution:
    def __init__(self):
        self.s = 0
    
    def convertBST(self, root):
        if root:
            self.convertBST(root.right)
            self.s += root.val
            root.val = self.s
            self.convertBST(root.left)
        return root