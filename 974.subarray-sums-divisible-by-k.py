#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#

# @lc code=start
class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        mod_hash = {0:1}
        ans = 0
        cur_sum = 0 
        n = len(A)
        for i in range(n):
            cur_sum += A[i]
            mod = cur_sum%K
            if mod in mod_hash:
                ans += mod_hash[mod]
            if mod not in mod_hash: 
                mod_hash[mod] = 0
            mod_hash[mod] +=1
        return ans
# @lc code=end

