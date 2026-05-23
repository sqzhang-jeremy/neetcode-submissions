class Solution:
    def isValid(self, s: str) -> bool:

        s_match = {')': '(', ']': '[', '}': '{'}
        stack = []
        
        for char in s:
            if char in s_match:
                if not stack or stack[-1] != s_match[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        return not stack
             