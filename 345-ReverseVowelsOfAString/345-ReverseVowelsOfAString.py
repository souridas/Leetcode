# Last updated: 2/21/2026, 9:43:53 AM
class Solution:
    def reverseVowels(self, s: str) -> str:
        def check_vowel(c):
            if c.lower() in ['a','e','i','o','u']:
                return True
            return False
        s_list=[s[i] for i in range(len(s))]
        i=0
        j=len(s)-1
        while(i<=j):
            if check_vowel(s[i]) and check_vowel(s[j]):
                temp=s_list[i]
                s_list[i]=s_list[j]
                s_list[j]=temp
                i+=1
                j-=1
            elif check_vowel(s[i]) and not check_vowel(s[j]):
                j-=1            
            elif not check_vowel(s[i]) and  check_vowel(s[j]):
                i+=1
            else:
                i+=1
                j-=1
        return ''.join(s_list)