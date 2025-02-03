class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pos = 0  # Pointer for the next position of a valid element
        
        for i in range(len(nums)):
            if nums[i] != val:  # Keep elements that are not equal to val
                nums[pos] = nums[i]
                pos += 1  
        
        return pos
