#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
class Solution:
    # faster when repeated call
    count_ls = list()
    n = 0 
    def countBits(self, num: int) -> List[int]:
        if num > self.n:
            diff = num - self.n 
            self.count_ls += [0] * (diff + 1)
            flag = 1
            for i in range(self.n+1, diff + 1):
                self.count_ls[i] = 1 + self.count_ls[i%flag]
                if i == flag << 1:
                    flag <<= 1
        self.n = num
        return self.count_ls[0: num+1]

    # standard method
    def countBits(self, num: int) -> List[int]:
        count_ls = [0] * (num + 1)
        #print(count_ls)
        flag = 1
        for i in range(1, num + 1):
            #print(i, flag,i%flag)
            count_ls[i] = 1 + count_ls[i%flag]
            if i == flag << 1:
                flag <<= 1
            #print(i, count_ls)
        return count_ls
