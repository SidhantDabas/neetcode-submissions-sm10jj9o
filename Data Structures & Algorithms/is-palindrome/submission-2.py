class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = 0
        s = "".join(filter(str.isalnum, s)).lower()
        
        for i in range(len(s)//2 + 1):
            if len(s) == 0:
                return True
            if s[i] == s[len(s)-1-i]:
                print("Char 1:", s[i], " Char 2:", s[len(s)-1-i])
                check += 1
            else:
                print("Char 1:", s[i], " Char 2:", s[len(s)-1-i])
                return False
        if check == len(s)//2 + 1:
            return True