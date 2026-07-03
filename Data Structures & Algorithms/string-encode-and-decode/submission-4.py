class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "0"
        ans = ""
        for i in strs:
            if i == None:
                return "0#"
            ans = ans + str(len(i)) + "#" + i
        return ans
    def decode(self, s: str) -> List[str]:
        if s == "0":
            return []
        ans = []
        initial = False
        cache = ""
        length = 0
        for i in s:
            if not initial:
                if i == '#':
                    length = int(cache)
                    if length == 0:
                        ans.append("")
                        cache = ""
                    else:
                        initial = True
                        cache = ""
                else:
                    cache += i
            else:
                if length != 0:
                    cache += i
                    length -= 1
                else:
                    ans.append(cache)
                    cache = str(i)
                    initial = False
        if cache != "":
            ans.append(cache)
        return ans