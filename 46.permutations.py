#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
class Solution:
    # easy to understand
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        path = []
        self.dfs(nums, path, res)
        return res
        
    
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)

    def permute(self, nums):
        perms = [[]]
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    new_perms.append(perm[:i] + [n] + perm[i:])  ###insert n
            perms = new_perms
        return perms


    # official answer
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0):
            # if all integers are used up
            if first == n:  
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first 
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        output = []
        backtrack()
        return output

    
    #memorization 
    hashmap = {}
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) < 2:
            return [nums]
        if tuple(nums) in self.hashmap:
            return self.hashmap[tuple(nums)]
        else:
            for i in range(1,len(nums)):            
                lefts = self.permute([nums[i]]) 
                rights = self.permute(nums[:i] + nums[i+1:])
                for l in lefts:
                    for r in rights:
                        if l+r not in ans:
                            ans.append(l+r)
                        if r+l not in ans:
                            ans.append(r+l)
        self.hashmap[tuple(nums)] = ans
        return ans
        
        
        

