"""
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
l1 = [2,4,3]
l1=l1[::-1]
l2 = [5,6,4]
l2=l2[::-1]
k=""
j=""

res = int("".join(map(str, l1)))
res2 = int("".join(map(str, l2)))
res3=res+res2
l=[int(x) for x in str(res3)]
print(l[::-1])

