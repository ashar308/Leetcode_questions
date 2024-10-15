class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        print("List is:")
        print(nums)
        print("\n")
        print("K is: ")
        print(k)
        dic = {}
        for i in nums:
            dic[i] = 1 + dic.get(i,0)
        #dic will have key value pair so 1-3 and 2-3 they both needed to 
be appended inside the list
        print("dic is")
        print(dic)
        lst = [[] for i in range(len(nums)+1)]

        for key,value in dic.items():
            lst[value].append(key)
        print("list is")
        print(lst)
        tmp = []
        for i in range(len(nums),-1,-1):
            if lst[i]:
                tmp.extend(lst[i])
            if len(tmp) == k:
                break
        print(tmp)
        return tmp

