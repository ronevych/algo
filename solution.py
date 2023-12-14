# Для бінарного дерева знайдіть суму всіх глибин усіх вузлів. Глибина вузла - це кількість ребер, які потрібно пройти від кореня дерева, щоб досягти цього вузла.

# Ваше завдання полягає в написанні функції, яка обчислює та повертає суми глибин для всіх вузлів у бінарному дереві

# Приклад: Розглянемо таке бінарне дерево:

#     1
#    / \
#   2   3
#  / \
# 4   5
# Глибина вузла 1 -0, глибина вузла 2 та 3 становить 1, а глибина вузлів 4 та 5 - 2. Сума глибин всіх вузлів дорівнює 0 + 1 + 1 + 2 + 2 = 6.

# Функція отримує на вхід корінь бінарного дерева, який має наступний вигляд:

# class TreeNode:
#     def __init__(self, value=0, left=None, right=None): root - це корінь бінарного дерева (1)
#         self.value = value
#         self.left = left
#         self.right = right

#  Ваша функція має мати такий вигляд:

# def sum_of_depths(root: TreeNode) -> int:
#     # ваш код
# Реалізація даної задачі не вимагає написання коду вставки чи виділення елементів з бінарного дерева. У тесті ви можете створити достатню кількість елементів класу TreeNode наступним чином:

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
#якщо ми знаємо кількість то щоб знайти

def sum_of_depths(root: TreeNode, current_depth=0) -> int:
    # if root is not None:
    #     print(root.value)
    if root is None:
        return 0
    return current_depth + sum_of_depths(root.left, current_depth + 1) + sum_of_depths(root.right, current_depth + 1)


#      3
#     / \
#    9    20

#   /   /  \
#  4   15   7
#            \
#            10


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
# root.right.right.right = TreeNode(10)
# root.left.left = TreeNode(4)
print(sum_of_depths(root))
