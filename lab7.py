import random
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def height(root):
    if root is None:
        return 0
    else:
        return 1 + max(height(root.left), height(root.right))

def imbalance(root):
    if root is None:
        return 0
    else:
        return abs(height(root.left) - height(root.right))

def generate_random_permutation():
    return random.sample(range(1, 21), 20)

def build_bst(permutation):
    root = None
    for num in permutation:
        root = insert(root, num)
    return root

def generate_histogram(data, title, xlabel, ylabel):
    plt.hist(data, bins=max(data)-min(data)+1, align='left')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def main():
    heights = []
    imbalances = []

    for _ in range(1000):
        permutation = generate_random_permutation()
        bst = build_bst(permutation)
        heights.append(height(bst))
        imbalances.append(imbalance(bst))

    generate_histogram(heights, "Height Histogram", "Height", "Frequency")
    generate_histogram(imbalances, "Imbalance Histogram", "Imbalance", "Frequency")

if __name__ == "__main__":
    main()
