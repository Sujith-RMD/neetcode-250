class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=""
        for i in range(len(strs[0])):
            for word in strs:
                if i>=len(word) or word[i]!=strs[0][i]:
                    return s
            s+=word[i]
        return s