class Solution(object):
    def maximumWealth(self, accounts):
        i=0
        m=[]
        while i < len(accounts):
             for j in range(0,len(accounts)):
                    m.append(sum(accounts[j]))
                    i=i+1
        return max(m)