class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            st_length = len(strs[i])
            strs[i] = str(st_length) + "#" + strs[i]
        encoded_string = "".join(strs)
        return encoded_string 


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j +=1
            length = int(s[i:j])
            res.append(s[j+ 1:j+1+length])
            i = j+1+length
        return res
        


        