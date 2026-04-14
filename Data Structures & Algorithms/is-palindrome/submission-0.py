class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            i_asc = ord(s[i].lower())
            j_asc = ord(s[j].lower())
            if i_asc < 48 or i_asc > 57 and i_asc < 97 or i_asc > 122:
                i += 1
                continue #is not a-z and 0-9 add and continue
            if j_asc < 48 or j_asc > 57 and j_asc < 97 or j_asc > 122:
                j -= 1
                continue #is not a-z and 0-9 add and continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True