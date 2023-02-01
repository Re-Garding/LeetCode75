"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
"""



def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    translator = {}

    for i in range(len(s)):
        if s[i] not in translator and t[i] in translator.values():
            return False
        if s[i] not in translator and t[i] not in translator.values():
            translator[s[i]] = t[i]
        if translator.get(s[i]) != t[i]:
            return False  
    
    return True 


s = 'badc'
t = 'baba'
print(isIsomorphic(s,t))

