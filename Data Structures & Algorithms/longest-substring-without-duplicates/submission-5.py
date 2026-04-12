class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = 0
        sub_s = ""
        for i in range(len(s)):
            if s[i] in  sub_s:
                sub_s = sub_s.split(s[i], 1)[-1]
            sub_s += s[i]
            s_len = max(len(sub_s), s_len)
            print(sub_s, "S_len ", s_len, "i", s[i])
        return s_len


    