#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
class Solution:

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            cur_nums = Solution().countAndSay(n-1)
            res = ""
            i = 0
            flag = 1 

            while i < len(cur_nums) :
                if  i == len(cur_nums) - 1:
                    res += str(flag) + cur_nums[i]
                    return res
                elif cur_nums[i] != cur_nums[i+1] :
                    res += str(flag) + cur_nums[i]
                    flag = 1
                elif cur_nums[i] == cur_nums[i+1]:
                    flag += 1
                i += 1
            return res
    #print(countAndSay(4))


