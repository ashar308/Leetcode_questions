class Solution:
    def unique(self, t: str) -> bool:
        dic = {}
        for s in t:
            dic[s] = 1+dic.get(s,0)
            if dic[s]>1:
                return False
        return True
    #unique("abac")

    def permutation(self, j:str, k:str) -> bool:
        dic1 = {}
        dic2 = {}
        for d in j:
            dic1[d] = 1 + dic1.get(d,0)
        print(dic1)
        for m in k:
            dic2[m] = 1 + dic2.get(m,0)
        print(dic2)
        if dic1 == dic2:
            return True
        return False
    def replace_space(self,j:str,length:int)-> str:
        tmp = ""
        for count in range(length):
            if j[count] == " ":
                tmp+= "%20"
            else:
                tmp+=j[count]
        return tmp
    def anagram_grp(self,lst:list[str]) -> list[int]:
        result = []
        dic = {}
        for word in lst:
            sort = ''.join(sorted(word))
            print("Sorted: ", sort)
            if sort not in dic:
                dic[sort] = []
            dic[sort].append(word)
        return dic.values()
    
    def palindrome_permutation(self,s:str)->bool:
        tmp_dic = {}
        count = 0
        for c in s:
            tmp_dic[c] = 1 + tmp_dic.get(c,0)
        odd_freq = 0
       
        for value in tmp_dic.items():
            print(value[1])
            print("value is: ",value)
            if value[1] % 2 != 0:
                odd_freq= odd_freq+1
            print("Odd frequency is: ",odd_freq)
        
        return odd_freq<=1
    

            
                

         
        


    
            




solution = Solution()
result = solution.unique("abac")
result1 = solution.unique("abc")
print(result)
print(result1)

#2 strings permutation of one another
result3 = solution.permutation("abc","cba")
print(result3)

result4 = solution.permutation("abcd","cba")
print(result4)

result5 = solution.replace_space("Mr John Smith  ",13)
print(result5)

result6 = solution.anagram_grp(["eat","tea","tan","ate","nat","bat"])
print(result6)

result7 = solution.palindrome_permutation("Tact Coa")
print("palindrome_permutation: ")
print(result7)
result8 = solution.palindrome_permutation("civic")
print("palindrome_permutation: ")
print(result8)
#abcdef
result9 = solution.palindrome_permutation("abcdef")
print("palindrome_permutation9: ")
print(result9)
#aabbccd

result10 = solution.palindrome_permutation("aabbccd")
print("palindrome_permutation10: ")
print(result10)
