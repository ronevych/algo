import unittest
from src.solution import *

class TestSolution(unittest.TestCase):
    def test_sum_of_depth(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        self.assertEqual(sum_of_depths(root), 2)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(sum_of_depths(root), 6)
        root.left.left = TreeNode(4)
        self.assertEqual(sum_of_depths(root), 8)
        root.right.right.right = TreeNode(10)
        self.assertEqual(sum_of_depths(root), 11)
        root.right.right.right.right = TreeNode(11)
        self.assertEqual(sum_of_depths(root), 15)
        root.right.right.right.right.right = TreeNode(12)
        self.assertEqual(sum_of_depths(root), 20)
        root.right.right.right.right.right.right = TreeNode(13)
        self.assertEqual(sum_of_depths(root), 26)
        root.right.right.right.right.right.right.right = TreeNode(14)
        self.assertEqual(sum_of_depths(root), 33)
        root.right.right.right.right.right.right.right.right = TreeNode(15)
        self.assertEqual(sum_of_depths(root), 41)
        root.right.right.right.right.right.right.right.right.right = TreeNode(16)
        self.assertEqual(sum_of_depths(root), 50)