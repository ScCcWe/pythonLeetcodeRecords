# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: dfs.py
# author: ScCcWe
# time: 2022/3/19 8:55 上午
from typing import Optional

"""
你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。

空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。

示例 1:

输入: 二叉树: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

输出: "1(2(4))(3)"

解释: 原本将是“1(2(4)())(3())”，
在你省略所有不必要的空括号对之后，
它将是“1(2(4))(3)”。
示例 2:

输入: 二叉树: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

输出: "1(2()(4))(3)"

解释: 和第一个示例相似，
除了我们不能省略第一个对括号来中断输入和输出之间的一对一映射关系。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-string-from-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "Node" + str(self.val)


class Solution:

    def dfs(self, root):
        if not root:
            return ""
        # print(root.left, root.right)

        if not root.left and not root.right:
            return f"{root.val}"

        # 这里使用了经典的内部result收集结果 + return出来的递归模式；可以多看看
        result = f"{root.val}"

        # 只有在左子树为空，但是右子树不为空时，需要加"()"
        if not root.left and root.right:
            result += "()"
            # print("not left: ", result)

        # 左子树不为空，则 ( dfs(left) )
        if root.left:
            result += "(" + self.dfs(root.left) + ")"
            # print("left: ", result)

        # 右子树不为空，则 ( dfs(right) )
        if root.right:
            result += "(" + self.dfs(root.right) + ")"
            # print("right: ", result)

        return result

    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.dfs(root)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)

    root.right = TreeNode(3)

    print(Solution().tree2str(root))
    print()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(4)

    root.right = TreeNode(3)

    print(Solution().tree2str(root))
