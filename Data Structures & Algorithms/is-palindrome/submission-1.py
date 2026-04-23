class Solution:
    def isPalindrome(self, s: str) -> bool:
        #if not  between A-Z or a-z or 0-9 or blank continue
        i = 0
        j = len(s) - 1
        while i < j:
            if not self.is_valid(s[i]):
                print(f"skipping {s[i]}")
                i += 1
                continue
            if not self.is_valid(s[j]):
                print(f"skipping {s[j]}")
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                print(f"{s[i]} != {s[j]}")
                return False
            i += 1
            j -= 1
        return True
            
    
    def is_valid(self, char):
        if (char.lower() >= 'a' and char.lower() <= 'z') or (char >= '0' and char <= '9'):
            return True
        return False
