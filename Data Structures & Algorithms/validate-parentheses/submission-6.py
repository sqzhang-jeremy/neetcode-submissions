class Solution:
    def isValid(self, s: str) -> bool:

        string_dict = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char not in string_dict:
                stack.append(char)
            else:
                if not stack or stack[-1] != string_dict[char]:
                    return False
                stack.pop()
                
        

                
        
        return not stack