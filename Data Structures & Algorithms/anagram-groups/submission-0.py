class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dic = {}
        for i,n in enumerate(strs):
            key = "".join(sorted(n))
            if key in str_dic:
                str_dic[key].append(n)
            else:
                str_dic[key] = [n]
        str_list = [value for key, value in str_dic.items()]
        return str_list