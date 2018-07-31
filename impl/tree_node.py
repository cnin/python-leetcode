#encoding=utf8

#ref: https://blog.csdn.net/jeason29/article/details/51585282
#ref: https://blog.csdn.net/jeason29/article/details/51518970

        
class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    @staticmethod
    def level_traversal(root):
        stack = [root]
        list_=[]
        
        while stack:
            current = stack.pop(0)
            list_.append(current.val)
            # print current.val
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

        return list_

    @staticmethod
    def pre_traversal(root):
        if not root:
            return
        print root.val
        TreeNode.pre_traversal(root.left)
        TreeNode.pre_traversal(root.right)
 
if __name__ == '__main__':
    tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6), TreeNode(7)))
    print(TreeNode.level_traversal(tree))
    # TreeNode.pre_traversal(tree)
