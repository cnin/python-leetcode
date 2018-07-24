#encoding=utf8
"""
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.经过替换之后的字符串为We%20Are%20Happy。
时间限制：1秒 空间限制：32768K 
"""

class Solution2:
    def replace_space(self, s):
        return s.replace(' ','%20')


"""
Another Solution:

    def replaceSpace(self, s):
        str_ = ''    
        for char in s:
            str_ = str_ + '%20' if char == ' ' else str_ + char
        return str_
"""