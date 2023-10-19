class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        matching = {')' : '(', '}' : '{', ']' : '['}

        for b in s:
            if b not in matching:
                stack.append(b)
            elif stack and stack[-1] == matching[b]:
                stack.pop()
            else:
                return False
        return len(stack) == 0