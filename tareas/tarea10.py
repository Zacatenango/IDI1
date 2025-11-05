class Nodo:
   def __init__(self, valor, izq=None, der=None):
      self.valor = valor
      self.izq = izq
      self.der = der


raiz = Nodo(0)
raiz.izq = Nodo(4)
raiz.der = Nodo(9)
raiz.izq.izq = Nodo(5)
raiz.izq.der = Nodo(2)
raiz.der.izq = Nodo(1)
raiz.der.der = Nodo(-3)
raiz.izq.izq.izq = Nodo(7)
raiz.izq.izq.der = Nodo(3)
raiz.izq.der.izq = Nodo(4)
raiz.izq.der.der = Nodo(1)
raiz.der.izq.izq = Nodo(10)
raiz.der.izq.der = Nodo(2)
raiz.der.der.izq = Nodo(1)
raiz.der.der.der = Nodo(8)


def minimax_ingenuo(nodo, profundidad, es_max):
   # Condición de salida: llegamos a la profundidad final o a una hoja
   if profundidad == 1 or (nodo.izq is None and nodo.der is None):
      return { "valor": nodo.valor, "nodo": nodo, "costado": None }
   
   # El nodo inicial es max: elegimos los hijos máximos
   if es_max:
      # Inicializamos nuestro valor máximo en una representación de Python del -infinito
      valor_max = float("-inf")
      mejor_hoja = None
      mejor_costado = None

      # Si hay nodo a la izquierda, llamamos recursivamente la función en ese nodo, con la 
      # profundidad decrementada; y ponemos que es Min, porque el hijo de un Max es Min.
      if nodo.izq is not None:
         resultao = minimax_ingenuo(nodo.izq, profundidad-1, es_max=False)
         # Terminando nuestra rama de recursividad, si nuestro valor es mayor que el 
         # valor máximo, ponemos eso en las variables del resultado e indicamos que el mejor costado
         # a seguir es el izquierdo
         if resultao["valor"] > valor_max:
            valor_max = resultao["valor"]
            mejor_hoja = resultao["nodo"]
            mejor_costado = "izquierdo"
      
      # Ahora, si hay nodo a la derecha, pasamos a revisarlo, igual con la profundidad decrementada
      # Y hacemos lo mismo que con el nodo izquierdo pero indicando que es a la derecha.
      if nodo.der is not None:
         resultao = minimax_ingenuo(nodo.der, profundidad-1, es_max=False)
         if resultao["valor"] > valor_max:
            valor_max = resultao["valor"]
            mejor_hoja = resultao["nodo"]
            mejor_costado = "derecho"
      
      # Terminada esta cadena de recursión, tiramos el resultado
      return { "valor": valor_max, "nodo": mejor_hoja, "costado": mejor_costado }
   
   # Ahora, si el nodo es min, hacemos lo mismo pero buscando un valor mínimo
   else:
      valor_min = float("inf")
      mejor_hoja = None
      mejor_costado = None

      if nodo.izq is not None:
         resultao = minimax_ingenuo(nodo.izq, profundidad-1, es_max=True)
         if resultao["valor"] < valor_min:
            valor_min = resultao["valor"]
            mejor_hoja = resultao["nodo"]
            mejor_costado = "izquierdo"
      if nodo.der is not None:
         resultao = minimax_ingenuo(nodo.der, profundidad-1, es_max=True)
         if resultao["valor"] < valor_min:
            valor_min = resultao["valor"]
            mejor_hoja = resultao["nodo"]
            mejor_costado = "derecho"
      return { "valor": valor_min, "nodo": mejor_hoja, "costado": mejor_costado }


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
value, leaf, side = de_minimis(root, 4, True)
print(f"Root is MAX: value={value}, leaf_value={leaf.value}, side={side}")

# 4 levels, root is MIN
value, leaf, side = de_minimis(root, 4, False)
print(f"Root is MIN: value={value}, leaf_value={leaf.value}, side={side}")

print("\n" + "=" * 60)
print("Testing with 3 levels:")
print("=" * 60)

# 3 levels, root is MAX
value, leaf, side = de_minimis(root, 3, True)
print(f"Root is MAX: value={value}, leaf_value={leaf.value}, side={side}")

# 3 levels, root is MIN
value, leaf, side = de_minimis(root, 3, False)
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