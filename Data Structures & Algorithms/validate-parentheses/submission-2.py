class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        for i in range(len(s)):
            char = s[i]
            if char == '(' or char == '{' or char == '[':
                ans.append(char)
            else:
                if len(ans) == 0:
                    return False
                if char == ")":
                    if ans[len(ans) - 1] == "(":
                        ans.pop()
                        continue
                    else:
                        return False
                elif char == "}":
                    if ans[len(ans) - 1] == "{":
                        ans.pop()
                        continue
                    else:
                        return False
                elif char == "]":
                    if ans[len(ans) - 1] == "[":
                        ans.pop()
                        continue
                    else:
                        return False
        return len(ans) == 0