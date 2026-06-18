class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        bracket_map = {")":"(", "]":"[", "}":"{"}
        stack = []

        for ch in s:
            if ch in bracket_map:
                if stack and stack[-1] == bracket_map[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return len(stack) == 0
                