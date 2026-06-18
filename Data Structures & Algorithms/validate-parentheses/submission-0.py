class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        bracket_map = {")":"(", "]":"[", "}":"{"}
        stack = []

        for ch in s:
            if ch in bracket_map.values():
                stack.append(ch)
            elif ch in bracket_map:
                if not stack or stack.pop() != bracket_map[ch]:
                    return False
        return len(stack) == 0
        