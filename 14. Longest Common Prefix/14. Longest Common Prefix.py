class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        lens = [len(str) for str in strs]
        min_len = min(lens)
        result = ''

        for i in range(1, min_len+1):
            prefix = strs[0][:i]
            for s in strs:
                if s[:i] != prefix:
                    return result
            result = prefix
        
        return result