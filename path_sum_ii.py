# https://leetcode.com/problems/path-sum-ii/description/
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1

class Tree:
  def __init__(self, x=None):
    self.val = x
    self.left = None
    self.right = None

  def __str__(self):
    return str(self.val)

  def insert_node(self, tree_list, root, i):
    if i < len(tree_list):
      root = Tree(tree_list[i])
      root.left = self.insert_node(tree_list, root.left, i*2+1)
      root.right = self.insert_node(tree_list, root.right, i*2+2)
    return root
    
  def pre_order(self, root, target_sum, path=[]):
    print('root is:', root, '\npath is:', path)
    if root != None and sum(path) <= target_sum:
      path.append(root.val)
      self.pre_order(root.left, target_sum, path)
      self.pre_order(root.right, target_sum, path)
      

class Solution:
  def pathSum(self, tree_list, target_sum):
    tree = Tree()
    tree_root = None
    tree_root = tree.insert_node(tree_list, tree_root, 0)
    tree.pre_order(tree_root, target_sum)


solution = Solution()
solution.pathSum([5,4,8,11,None,13,4,7,2,None,None,5,1], 22)