import json

class TreeNode:
    """Represents a node in the binary tree"""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    @classmethod
    def from_dict(cls, data):
        """Construct a tree from a dictionary/JSON structure"""
        if data is None:
            return None
        if isinstance(data, (int, float)):
            # Leaf node
            return cls(data)
        
        value = data['value']
        left = cls.from_dict(data.get('left'))
        right = cls.from_dict(data.get('right'))
        return cls(value, left, right)


def minimax(node, depth, is_max_node):
    """
    Minimax algorithm implementation
    
    Args:
        node: Current tree node
        depth: Number of levels remaining to analyze
        is_max_node: True if current node is a MAX node, False for MIN node
    
    Returns:
        tuple: (best_value, best_leaf_node, side)
            - best_value: The minimax value
            - best_leaf_node: The leaf node chosen by the algorithm
            - side: 'left' or 'right' indicating which side of root the leaf is on
    """
    # Base case: reached target depth or leaf node
    if depth == 1 or (node.left is None and node.right is None):
        return (node.value, node, None)
    
    if is_max_node:
        # MAX node: choose maximum of children
        max_value = float('-inf')
        best_leaf = None
        best_side = None
        
        if node.left is not None:
            left_value, left_leaf, _ = minimax(node.left, depth - 1, False)
            if left_value > max_value:
                max_value = left_value
                best_leaf = left_leaf
                best_side = 'left'
        
        if node.right is not None:
            right_value, right_leaf, _ = minimax(node.right, depth - 1, False)
            if right_value > max_value:
                max_value = right_value
                best_leaf = right_leaf
                best_side = 'right'
        
        return (max_value, best_leaf, best_side)
    
    else:
        # MIN node: choose minimum of children
        min_value = float('inf')
        best_leaf = None
        best_side = None
        
        if node.left is not None:
            left_value, left_leaf, _ = minimax(node.left, depth - 1, True)
            if left_value < min_value:
                min_value = left_value
                best_leaf = left_leaf
                best_side = 'left'
        
        if node.right is not None:
            right_value, right_leaf, _ = minimax(node.right, depth - 1, True)
            if right_value < min_value:
                min_value = right_value
                best_leaf = right_leaf
                best_side = 'right'
        
        return (min_value, best_leaf, best_side)


# Example usage with the provided tree
tree_json = {
   "value": 0,
   "left": {
      "value": 4,
      "left": {
         "value": 5,
         "left": 7,
         "right": 3
      },
      "right": {
         "value": 2,
         "left": 4,
         "right": 1
      }
   },
   "right": {
      "value": 9,
      "left": {
         "value": 1,
         "left": 10,
         "right": 2
      },
      "right": {
         "value": -3,
         "left": 1,
         "right": 8
      }
   }
}

# Build the tree
root = TreeNode.from_dict(tree_json)

# Test cases
print("=" * 60)
print("Testing with 4 levels:")
print("=" * 60)

# 4 levels, root is MAX
value, leaf, side = minimax(root, 4, True)
print(f"Root is MAX: value={value}, leaf_value={leaf.value}, side={side}")

# 4 levels, root is MIN
value, leaf, side = minimax(root, 4, False)
print(f"Root is MIN: value={value}, leaf_value={leaf.value}, side={side}")

print("\n" + "=" * 60)
print("Testing with 3 levels:")
print("=" * 60)

# 3 levels, root is MAX
value, leaf, side = minimax(root, 3, True)
print(f"Root is MAX: value={value}, leaf_value={leaf.value}, side={side}")

# 3 levels, root is MIN
value, leaf, side = minimax(root, 3, False)
print(f"Root is MIN: value={value}, leaf_value={leaf.value}, side={side}")
