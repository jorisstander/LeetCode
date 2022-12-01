class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a, b = 0, 0
        v = set('aioueAIOUE')
        for i in range(len(s)//2):
            if s[i] in v:
                a+=1
            if s[-i-1] in v:
                b+=1
        
        return a==b
