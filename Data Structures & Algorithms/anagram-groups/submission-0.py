class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        output = []
        for i in range(0, len(strs)):
            t = tuple(sorted(strs[i]))

            if hashmap.get(t) is None:
                hashmap[t] = [i]
            else:
                hashmap[t].append(i)
        
        for val in hashmap.values():
            j = []
            for i in range(0, len(val)):
                j.append(strs[val[i]])
            output.append(j)
        
        return output


