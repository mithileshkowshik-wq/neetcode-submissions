class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        satisfied = False
        nums2 = nums.copy()
        nums.sort()

        while satisfied == False:
            if (nums[l] + nums[r]) > target:
                r = r - 1
            elif (nums[l] + nums[r]) < target:
                l = l + 1
            else:
                satisfied = True
                idx_l = nums2.index(nums[l])
                nums2[idx_l] = 'g'
                idx_r = nums2.index(nums[r])
                output = [idx_l, idx_r]
                output.sort()
                return output
