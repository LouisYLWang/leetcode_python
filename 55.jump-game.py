#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# Java

class Solution {
    // method 1 greedy
    public boolean canJump(int[] nums) {
        int n = nums.length;
        int cur = nums[n - 1];
        for (int i = n-1; i >= 0; i--){
            if (i + nums[i] >= cur){
                cur = i;
            }
        }
        return cur == 0;
    }

        
    // method 2 dp from top to down
    public boolean canJump(int[] nums) {
        int n = nums.length;
        nums[n - 1] = -1;
        for (int i = n - 2; i >= 0; i --){
            for (int j = 0; j < nums[i] + 1; j ++){
                //System.out.println("i "+i+" j "+j);
                if (i+j < n && nums[i] >= 0 && nums[i + j] < 0){
                    nums[i] *= -1;
                }
            }
        }
        
        for (int num: nums){
            //System.out.print(num);
        }
        
        return nums[0] < 0;
    }
}



# Py
class Solution:
    # top down dp, self solition exceed time limit
    '''
    def canJump(self, nums: List[int]) -> bool:
        nums[-1] = -1

        for i in range(len(nums)-2, -1, -1):
            for j in range(nums[i]+1):
                if i+j < len(nums) and nums[i] >= 0 and nums[i+j] < 0:
                    nums[i] *= -1

        return nums[0] < 0 
    '''
    
    # greedy: push the boundary left, iterate back and once reach boundary, reset the boundary line
    
    def canJump(self, nums: List[int]) -> bool:
        cur = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            
            # once reach, reset the bound
            if i + nums[i] >= cur:
                cur = i

        return cur == 0

