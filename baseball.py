from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = 0
        tmp = []
        for i in operations:
            if i == "+":
                tmp.append(tmp[-1]+tmp[-2])
            elif  i == "D":
                tmp.append(tmp[-1]*2)
            elif i == "C":
                tmp.pop()
            else:
                tmp.append(int(i))
        return sum(tmp)
