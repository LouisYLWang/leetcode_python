#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
class Solution:
    # notice:
    # do not use [object] * n to generate object list
    # slow but worked, pruning using sort
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        backtracing = []
        for i in range(target):
            backtracing.append([])

        for tar in range(1,target+1):
            for cand in candidates:
                if cand == tar:
                    backtracing[tar-1].append([cand])
                if cand < tar:
                    if backtracing[tar - cand - 1]:
                        for i in backtracing[tar - cand - 1]:
                            cur = i + [cand]
                            cur.sort()
                            if cur not in backtracing[tar - 1]:
                                backtracing[tar - 1].append(cur)

                        
        return backtracing[target-1]


       
