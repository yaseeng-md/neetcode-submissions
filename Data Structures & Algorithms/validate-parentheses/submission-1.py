class Solution:
    def isValid(self, s: str) -> bool:
        charmap = {"}" : "{", ")" : "(", "]" : "["}
        stack = []

        for char in s:
            # if we have found ending loop, look for start in stack
            if char in charmap.keys():
                if len(stack) == 0:
                    return False

                if charmap.get(char) != stack.pop():
                    return False
            else:
                stack.append(char)
        return True if len(stack) == 0 else False
        