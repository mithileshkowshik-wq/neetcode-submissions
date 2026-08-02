class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        
        sorted_nums = sorted(nums)
        seq = 1
        maxseq = 0
        for i in range(0, len(nums)-1):
            if (sorted_nums[i+1]) == (sorted_nums[i]+1):
                seq += 1
                maxseq = max(maxseq, seq)
                
            elif sorted_nums[i] == sorted_nums[i + 1]:
                seq = seq
                maxseq = max(maxseq, seq)
            else:
                maxseq = max(maxseq, seq)
                seq = 1
        return maxseq


        