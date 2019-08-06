#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#
class Solution:
    # common method
    def fizzBuzz(self, n: int) -> List[str]:
        ans = list()
        for i in range(1, n + 1):
            if not i %3 and not i%5:
                ans.append("FizzBuzz")
            elif not i%5:
                ans.append("Buzz")
            elif not i%3:
                ans.append("Fizz")
            else:
                ans.append(str(i))
        return ans

    # use hash to reduce control statement, but slower
    def fizzBuzz(self, n: int) -> List[str]:
        fb_hash ={3:"Fizz", 5:"Buzz"}
        ans = []
        for i in range(1, n + 1):
            temp_ans = ""
            for key in fb_hash:
                if not i%key:
                    temp_ans += fb_hash[key]
            if not temp_ans:
                temp_ans += str(i)
            ans.append(temp_ans)
        return ans


