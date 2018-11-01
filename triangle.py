'''
https://leetcode.com/problems/triangle/
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''

class Solution:
    def minimumTotal(self, triangle):
        min_length, n, row = triangle[len(triangle)-1], len(triangle)-2, []
        for row in range(n, -1, -1):
            for i in range(len(triangle[row])):
                min_length[i] = min(min_length[i], min_length[i+1]) + triangle[row][i]
        return min_length[0]
        


############### Example #################
#                           [
#                                [2],
#                               [3,4],
#                              [6,5,7],
#                             [4,1,8,3]
#                           ]

#               min_length == [4,1,8,3]
# i=0, row=2 -> min_length == [7,1,8,3]
# i=1, row=2 -> min_length == [7,6,8,3]
# i=2, row=2 -> min_length == [7,6,10,3]

# i=0, row=1 -> min_length == [9,6,10,3]
# i=1, row=1 -> min_length == [9,10,10,3]

# i=0, row=0 -> min_length == [11,10,10,3]