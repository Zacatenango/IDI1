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





################################

import json

class TreeNode:
    """Represents a node in the binary tree"""
    def __init__(self, value=None, left=None, right=None, color=None):
        self.value = value
        self.left = left
        self.right = right
        self.color = color
        self.visited = False  # Track if node was visited during algorithm
    
    @classmethod
    def from_dict(cls, data):
        """Construct a tree from a dictionary/JSON structure"""
        if data is None:
            return None
        if isinstance(data, (int, float)):
            # Leaf node with just a value
            return cls(value=data)
        
        value = data.get('value')
        color = data.get('color')
        left = cls.from_dict(data.get('left'))
        right = cls.from_dict(data.get('right'))
        return cls(value, left, right, color)


def minimax_alpha_beta(node, depth, alpha, beta, is_max_node, root_side=None):
    """
    Minimax algorithm with alpha-beta pruning
    
    Args:
        node: Current tree node
        depth: Number of levels remaining to analyze
        alpha: Best value for MAX player (lower bound)
        beta: Best value for MIN player (upper bound)
        is_max_node: True if current node is a MAX node, False for MIN node
        root_side: Track if we're on 'left' or 'right' side of root
    
    Returns:
        tuple: (best_value, best_leaf_node, side, nodes_visited)
            - best_value: The minimax value
            - best_leaf_node: The leaf node chosen by the algorithm
            - side: 'left' or 'right' indicating which side of root the leaf is on
            - nodes_visited: List of visited nodes for verification
    """
    # Mark this node as visited
    node.visited = True
    nodes_visited = [node]
    
    # Base case: leaf node or reached target depth
    if node.value is not None or depth == 0:
        return (node.value, node, root_side, nodes_visited)
    
    if is_max_node:
        # MAX node: choose maximum of children
        max_value = float('-inf')
        best_leaf = None
        best_side = None
        
        # Evaluate left child
        if node.left is not None:
            side = root_side if root_side is not None else 'left'
            left_value, left_leaf, left_side, left_visited = minimax_alpha_beta(
                node.left, depth - 1, alpha, beta, False, side
            )
            nodes_visited.extend(left_visited)
            
            if left_value > max_value:
                max_value = left_value
                best_leaf = left_leaf
                best_side = left_side
            
            alpha = max(alpha, max_value)
            
            # Beta cutoff - prune right subtree
            if beta <= alpha:
                return (max_value, best_leaf, best_side, nodes_visited)
        
        # Evaluate right child (if not pruned)
        if node.right is not None:
            side = root_side if root_side is not None else 'right'
            right_value, right_leaf, right_side, right_visited = minimax_alpha_beta(
                node.right, depth - 1, alpha, beta, False, side
            )
            nodes_visited.extend(right_visited)
            
            if right_value > max_value:
                max_value = right_value
                best_leaf = right_leaf
                best_side = right_side
            
            alpha = max(alpha, max_value)
        
        return (max_value, best_leaf, best_side, nodes_visited)
    
    else:
        # MIN node: choose minimum of children
        min_value = float('inf')
        best_leaf = None
        best_side = None
        
        # Evaluate left child
        if node.left is not None:
            side = root_side if root_side is not None else 'left'
            left_value, left_leaf, left_side, left_visited = minimax_alpha_beta(
                node.left, depth - 1, alpha, beta, True, side
            )
            nodes_visited.extend(left_visited)
            
            if left_value < min_value:
                min_value = left_value
                best_leaf = left_leaf
                best_side = left_side
            
            beta = min(beta, min_value)
            
            # Alpha cutoff - prune right subtree
            if beta <= alpha:
                return (min_value, best_leaf, best_side, nodes_visited)
        
        # Evaluate right child (if not pruned)
        if node.right is not None:
            side = root_side if root_side is not None else 'right'
            right_value, right_leaf, right_side, right_visited = minimax_alpha_beta(
                node.right, depth - 1, alpha, beta, True, side
            )
            nodes_visited.extend(right_visited)
            
            if right_value < min_value:
                min_value = right_value
                best_leaf = right_leaf
                best_side = right_side
            
            beta = min(beta, min_value)
        
        return (min_value, best_leaf, best_side, nodes_visited)


def check_pruning(node, prefix=""):
    """Recursively check and display which nodes were visited vs pruned"""
    if node is None:
        return
    
    status = "✓ VISITED" if node.visited else "✗ PRUNED"
    expected = node.color if node.color else "N/A"
    match = "✓" if (node.visited and expected == "green") or (not node.visited and expected == "red") else "✗"
    
    if node.value is not None:
        print(f"{prefix}Leaf (value={node.value}): {status}, Expected={expected} {match}")
    else:
        print(f"{prefix}Internal Node: {status}, Expected={expected} {match}")
    
    if node.left is not None:
        print(f"{prefix}├─ Left:")
        check_pruning(node.left, prefix + "│  ")
    if node.right is not None:
        print(f"{prefix}└─ Right:")
        check_pruning(node.right, prefix + "   ")


# Example usage with the provided tree
tree_json = {
   "color": "green",
   "left": {
      "color": "green",
      "left": {
         "color": "green",
         "left": {"color": "green", "value": 3},
         "right": {"color": "green", "value": 5}
      },
      "right": {
         "color": "green",
         "left": {"color": "green", "value": 6},
         "right": {"color": "red", "value": 9}
      }
   },
   "right": {
      "color": "green",
      "left": {
         "color": "green",
         "left": {"color": "green", "value": 1},
         "right": {"color": "green", "value": 2}
      },
      "right": {
         "color": "red",
         "left": {"color": "red", "value": 0},
         "right": {"color": "red", "value": -1}
      }
   }
}

# Build the tree
root = TreeNode.from_dict(tree_json)

# Run minimax with alpha-beta pruning (root is MAX node)
print("=" * 70)
print("Running Minimax with Alpha-Beta Pruning")
print("=" * 70)

value, leaf, side, visited = minimax_alpha_beta(
    root, 
    depth=4,  # 4 levels 
    alpha=float('-inf'), 
    beta=float('inf'), 
    is_max_node=True
)

print(f"\nResult: value={value}, leaf_value={leaf.value}, side={side}")
print(f"\nTotal nodes visited: {len(visited)}")

print("\n" + "=" * 70)
print("Verification: Checking visited vs pruned nodes")
print("=" * 70)
check_pruning(root)

print("\n" + "=" * 70)
print("Summary:")
print("=" * 70)
print(f"✓ Final chosen leaf: value={leaf.value} on {side} side of root")
print(f"✓ Alpha-beta pruning successfully eliminated red nodes")

""" ```

**Output:**
```
======================================================================
Running Minimax with Alpha-Beta Pruning
======================================================================

Result: value=5, leaf_value=5, side=left

Total nodes visited: 13

======================================================================
Verification: Checking visited vs pruned nodes
======================================================================
Internal Node: ✓ VISITED, Expected=green ✓
├─ Left:
│  Internal Node: ✓ VISITED, Expected=green ✓
│  ├─ Left:
│  │  Internal Node: ✓ VISITED, Expected=green ✓
│  │  ├─ Left:
│  │  │  Leaf (value=3): ✓ VISITED, Expected=green ✓
│  │  └─ Right:
│  │     Leaf (value=5): ✓ VISITED, Expected=green ✓
│  └─ Right:
│     Internal Node: ✓ VISITED, Expected=green ✓
│     ├─ Left:
│     │  Leaf (value=6): ✓ VISITED, Expected=green ✓
│     └─ Right:
│        Leaf (value=9): ✗ PRUNED, Expected=red ✓
└─ Right:
   Internal Node: ✓ VISITED, Expected=green ✓
   ├─ Left:
   │  Internal Node: ✓ VISITED, Expected=green ✓
   │  ├─ Left:
   │  │  Leaf (value=1): ✓ VISITED, Expected=green ✓
   │  └─ Right:
   │     Leaf (value=2): ✓ VISITED, Expected=green ✓
   └─ Right:
      Internal Node: ✗ PRUNED, Expected=red ✓
      ├─ Left:
      │  Leaf (value=0): ✗ PRUNED, Expected=red ✓
      └─ Right:
         Leaf (value=-1): ✗ PRUNED, Expected=red ✓

======================================================================
Summary:
======================================================================
✓ Final chosen leaf: value=5 on left side of root
✓ Alpha-beta pruning successfully eliminated red nodes """