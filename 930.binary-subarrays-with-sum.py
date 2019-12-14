#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#

# @lc code=start
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        sum_hash = {0:1}
        cursum = 0
        ans = 0
        
        for a in A:
            cursum += a
            ans += sum_hash.get(cursum - S,0)

            if cursum not in sum_hash:
                sum_hash[cursum] = 0
            sum_hash[cursum] += 1
            
        return ans# @lc code=end

