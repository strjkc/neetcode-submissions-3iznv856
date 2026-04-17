class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = { "}": "{", "]": "[", ")": "("}

        for char in s:
            if char in brackets and stack:
                    if brackets[char] == stack[-1]:
                        stack.pop()
                    else:
                        return False
            else:
                stack.append(char)
        return len(stack) == 0
        