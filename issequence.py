class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:  # If `s` is empty, it's a subsequence of any string
            return True
        
        # Pointer for `s`
        s_pointer = 0

        for char in t:
            if char == s[s_pointer]:
                s_pointer += 1
            if s_pointer == len(s):  # All characters in `s` are matched
                return True
        
        return s_pointer == len(s)  # Return true if all characters were matched


