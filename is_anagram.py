class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #two dictionaries
        dic1 = {}
        dic2 = {}
        for m in s:
            dic1[m] = 1+dic1.get(m,0)
        for k in t:
            dic2[k] = 1+dic2.get(k,0)
        if dic1==dic2:
            return True
        else:
            return False
        
