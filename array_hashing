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
            res[tuple(res)].append(s)
        return res.values()
    

                    