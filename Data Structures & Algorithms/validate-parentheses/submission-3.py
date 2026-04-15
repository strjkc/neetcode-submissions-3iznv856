class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        br_map = { ")": "(", "}": "{", "]": "["}
        for br in s:
            if br in br_map and stack:
                if stack[-1] == br_map[br]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(br)
        return True if len(stack) == 0 else False