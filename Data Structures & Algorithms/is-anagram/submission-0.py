class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1=dict()
        h2=dict()
        for i in s:
            if i in h1.keys():
                x=h1[i]
                h1[i]=x+1
            else:
                h1[i]=1
        for i in t:
            if i in h2.keys():
                x=h2[i]
                h2[i]=x+1
            else:
                h2[i]=1
                
        if len(h1)!= len(h2):
            return False

        for i in h1.keys():
            if i not in h2.keys():
                return False
            elif h1[i]!=h2[i]:
                return False
        return True