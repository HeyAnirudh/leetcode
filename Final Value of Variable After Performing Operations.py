"""
Input: operations = ["--X","X++","X++"]
Output: 1
Explanation: The operations are performed as follows:
Initially, X = 0.
--X: X is decremented by 1, X =  0 - 1 = -1.
X++: X is incremented by 1, X = -1 + 1 =  0.
X++: X is incremented by 1, X =  0 + 1 =  1.
"""
arr=["--X","X++","X++"]
k=[]
for i in range(0,len(arr)):
    if arr[i]=="X++" or arr[i]=="++X":
        k.append(1)
    elif arr[i]=="X--" or arr[i]=="--X":
        k.append(-1)
print(sum(k))