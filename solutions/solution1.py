#encoding=utf8
"""
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
时间限制：1秒 空间限制：32768K
"""

class Solution1(object):
    def find(self, target, array):
        nrow = len(array)
        ncol = len(array[0])
        row = 0
        col = ncol-1
        while row<nrow and col>=0:
            if target == array[row][col]:
                return True
            elif target > array[row][col]:
                row += 1
            else:
                col -= 1
        return False

    def find_alter(self, target, array):
        flag = False
        for index in range(len(array)):
            if target in array[index]:
                flag = True
        return flag


