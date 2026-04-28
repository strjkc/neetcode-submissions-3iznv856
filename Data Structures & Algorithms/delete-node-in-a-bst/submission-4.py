# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        curr = root
        def _del(node, val):
            if not node:
                return None
            if val > node.val:
                node.right = _del(node.right, val)
                return node
            elif val < node.val:    
                node.left = _del(node.left, val)
                return node
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                io_repl = get_repl(node.right)
                node.val = io_repl.val
                node.right = _del(node.right, node.val)
                return node
        def get_repl(curr):
            while curr.left:
                curr = curr.left
            return curr
        return _del(curr, key)
