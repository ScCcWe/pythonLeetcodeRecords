# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: 答案.py
# author: ScCcWe
# time: 2022/3/23 10:00 上午
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.set_item = set()

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """
        leetcode答案给的这种解法，算是将dfs和需求逻辑有效的结合了；

        可能你会有这样的疑问：如果root的第一个数(即：根节点)就满足，但是此时`set_item`中没有存放相应的target，这样不就False了吗？
            其实不用担心，既然第一个数满足，那么说明root中肯定存在target；
            在不断的递归之后，总是能遍历到target的，将它记为Node1；这时候，Node1需要的target就是第一个数
        """

        """
        1）初始树为None，（这个在本题中不满足，因为规定了root的节点数 >= 1  
        
        2）左子树为空，则返回False
        
        3）右子树为空，则返回False
        
        》值得注意的是，这里的False并不是最终的返回结果；
        》最终还是要看 return self.findTarget(root.left, k) or self.findTarget(root.right, k)
        》何时真的返回False？
        》   递归到了叶子节点 + 左右子树都为None （缺一不可，如果没到叶子节点，递归还是会进行；就永远不满足左右都为None
        """
        if root is None:
            return False

        # 找到了满足条件的值，结束
        if k - root.val in self.set_item:
            return True

        # 当前节点的值入集合，方便下一次递归判断使用
        self.set_item.add(root.val)

        # 使用递归查找，来判断`当前节点的左子节点`或`右子节点`是否满足
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)


if __name__ == '__main__':
    tree = TreeNode(1)
    # tree.left = TreeNode(1)

    print(Solution().findTarget(tree, 2))
