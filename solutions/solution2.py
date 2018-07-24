#encoding=utf8
"""
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.经过替换之后的字符串为We%20Are%20Happy。
时间限制：1秒 空间限制：32768K 
"""

class Solution2(object):
    def replace_space(self, s):
        return s.replace(' ','%20')

    def replace_space_alter(self, s):
        str_ = ''    
        for char in s:
            str_ = str_ + '%20' if char == ' ' else str_ + char
        return str_

    #根据python代码规范 
    #应当尽可能少的使用+=来组合字符串
    #规范推荐使用join list方法
    #http://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#id12
    
    def replace_space_alter_2(self, s):
        str_list = []    
        for char in s:
            str_list.append('%20' if char == ' ' else char)
        return ''.join(str_list)