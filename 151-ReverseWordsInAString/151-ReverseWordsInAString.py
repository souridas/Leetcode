# Last updated: 2/21/2026, 9:44:24 AM
class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split(' ')
        words=[word.strip(' ') for word in words]
        new_words=[]
        for word in words:
            if word!='':
                new_words.append(word)
        new_words.reverse()
        
        answer=""
        for i in range(len(new_words)):
            if new_words[i]!='':
                answer+=new_words[i]
                if i!=len(new_words)-1:
                    answer+=" "

        return answer
            

        