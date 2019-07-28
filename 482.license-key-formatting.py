#
# @lc app=leetcode id=482 lang=python
#
# [482] License Key Formatting
#
class Solution(object):
  def licenseKeyFormatting(self, S, K):
        x = 0
        S = S.replace("-", "").upper()
        mod = len(S) % K
        if mod == 0:
            mod += K
        while mod < len(S):
            S = S[:mod] + "-" + S[mod:]
            mod += K + 1
        return S

