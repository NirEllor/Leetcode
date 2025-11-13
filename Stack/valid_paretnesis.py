class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left_to_right = {'(' : ')', '{': '}', '[' : ']'}
        for c in s:
            if c in left_to_right:
                stack.append(c)
            else:
                if not stack:
                    return False
                prev = stack.pop()
                if c != left_to_right[prev]:
                    return False

        return not stack


s = Solution()
print(s.isValid("()[{}"))