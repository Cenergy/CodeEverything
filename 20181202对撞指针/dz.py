# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '2/12/2018 10:29 PM'


def lengthOfLongestSubstring(s):
    freq = {}
    l = 0
    r = -1
    res = 0

    while (l < len(s)):

        if (r + 1 < len(s) and freq.get(s[r + 1], 0) == 0):
            freq[s[r + 1]] = freq.get(s[r + 1], 0) + 1
            r = r + 1
        else:
            freq[s[l]] = freq.get(s[l], 0) - 1
            l = l + 1
        res = max(res, r - l + 1)
    return res


if __name__ == '__main__':
    #LeetCode3
    # Input: "abcabcbb"
    # Output: 3
    # Explanation: The
    # answer is "abc",
    # with the length of 3.
    s = "abcdedhsjavdhsvdedadbjxzxnabcba"
    print(lengthOfLongestSubstring(s))
    a={}