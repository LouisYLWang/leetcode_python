def lengthOfLongestSubstring(s: str) -> int:
    max_len = 0
    cache = 0
    s_dic = {}
    for i in s:
        if i in s_dic:
            cache = 1
            s_dic = {}
            s_dic[i] = 1
        else:
            s_dic[i] = 1
            cache += 1
        max_len = max(cache, max_len)
        print(cache, max_len)
        print(s_dic)
    return max_len

lengthOfLongestSubstring("bbbbbb")