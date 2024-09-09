class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def constructMaximumBinaryTree(nums):
    if not nums:
        return None

    max_val = max(nums)
    max_idx = nums.index(max_val)

    root = TreeNode(max_val)


    root.left = constructMaximumBinaryTree(nums[:max_idx])


    root.right = constructMaximumBinaryTree(nums[max_idx + 1:])

    return root

nums = [3, 2, 1, 6, 0, 5]
root = constructMaximumBinaryTree(nums)

def printTree(node, level=0):
    if node is not None:
        printTree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.val)
        printTree(node.left, level + 1)

printTree(root)
