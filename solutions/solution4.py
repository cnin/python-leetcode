#encoding=utf8

"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，
重建二叉树并返回。
"""

from impl import TreeNode

class Solution4(object):

    def get_root_index(self, val_, list_):

        for index in range(len(list_)):
            # print(val_,list_)
            if val_ == list_[index]:
                return index
    
    def reconstruct_binary_tree(self, pre_, in_):
        root = TreeNode(pre_[0])
        root_index = self.get_root_index(root.val, in_)
        del pre_[0]
        del in_[root_index]
        if root_index>0:
            root.left = self.reconstruct_binary_tree(pre_[:root_index], in_[:root_index])
        if root_index<len(pre_):
            root.right = self.reconstruct_binary_tree(pre_[root_index:],in_[root_index:])
        return root


            