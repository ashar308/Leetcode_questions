class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        tmparr = [0]*len(arr)
        rightmax = -1
        for i in range(len(arr)-1,-1,-1):
            tmp = max(arr[i],rightmax)
            tmparr[i] = rightmax
            rightmax = tmp
        return tmparr
