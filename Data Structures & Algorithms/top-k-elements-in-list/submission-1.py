class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        output = []

        for i in range(0, len(nums)):
            if hashmap.get(nums[i]) is None:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
        
        sorted_dict = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))

        keys = list(sorted_dict.keys())
        for j in range(0, k):
            output.append(keys[j])
        
        output.sort()
        return output
        
            


        