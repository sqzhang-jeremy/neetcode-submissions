class Solution:
    def isValid(self, s: str) -> bool:

        string_dict = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if stack and char in string_dict and string_dict[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        

                
        
        return not stack
        