from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        str_lens = [len(s) for s in strs]
        # basestr = str_lens.index(min(str_lens))
        min(str_lens)

        prefix = ""

        for i in range(min(str_lens)):
            # check eachstr[i] == each other
            char = strs[0][i]
            if all([s[i] == char for s in strs]):
                prefix += char
        return prefix


Solution().longestCommonPrefix(["flower", "flow", "flight"])
Solution().longestCommonPrefix(["dog", "racecar", "car"])

