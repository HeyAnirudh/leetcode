class Solution(object):
    def reversePrefix(self, word, ch):
        st=""
        k=""
        n=0
        if ch in word:
            for i in range(0,len(word)):
                if word[i]==ch and n==0:
                    st=st+word[:i+1]
                    k=k+word[i+1:len(word)+1]
                    n+=1
            return(st[::-1]+k)
        else:
            return(word)