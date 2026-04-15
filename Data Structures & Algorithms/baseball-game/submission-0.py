class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation == "+":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2)
                stack.append(n1)
                stack.append(n1 + n2)
            elif operation == "C":
                stack.pop()
            elif operation == "D":
                n1 = stack.pop()
                stack.append(n1)
                stack.append(n1 * 2)      
            else:
                stack.append(int(operation))
        return sum(stack)