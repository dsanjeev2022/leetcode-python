#group anagrams
def groupAnagrams(self, strs):
    # creating a dictionary where the key is the an list of each
    # character instances
    res = defaultdict(list)
    for s in strs:
        #creating a key
        count = [0] * 26
        for c in s:
            count [ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)
    return res.values()
        
#product of array except self
def productExceptSelf(self, nums: List[int]) -> List[int]:
    res = [1] * len(nums)
    
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
        
    postfix = 1
    for i in range(len(nums),-1,-1,-1):
        res[i] *= postfix
        postfix *- nums[i]
    return res
    
#Longest Consecutive Sequence
def longestConsecutive(self, nums: List[int]) -> int:
    numset = set(nums)
    longest = 0
    
    for n in nums:
        #check if its the start of the sequence
        if (n-1) not in numset:
            length = 0
            while (n + length) in numset:
                length += 1
            longest = max(length, longest)
        return lomgest
        
 