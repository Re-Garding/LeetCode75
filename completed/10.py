"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
"""

def longestPalindrome(string):

    letters = {}

    for ch in string:
        letters[ch] = letters.get(ch, 0) + 1

    length = 0
    single = 0

    for num in letters.values():
        if num % 2 == 0:
            length += num
        if num % 2 != 0:
            length += (num//2)*2
        if num == 1 or num % 2 == 1 and single < 1:
            single = 1
    return single + length 



print(longestPalindrome("ccc"))