class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        product = 1
        zerocount = 0

        for i in range(0, len(nums)):
            if nums[i] == 0:
                zerocount += 1
        if zerocount >= 2:
            for i in range(0, len(nums)):
                output.append(0)
            return output
        elif zerocount == 1:
            for i in range(0, len(nums)):
                if nums[i] != 0:
                    output.append(0)
                else:
                    for j in range(0, len(nums)):
                        if nums[j] != 0:
                            product = product*nums[j]
                    output.append(product)
            return output
        else:
            for i in range(0, len(nums)):
                product = 1
                for j in range(0, len(nums)):
                    if i != j:
                        product = product * nums[j]
                output.append(product)
                
            return output

        