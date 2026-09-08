"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # A smaller value than the current node must go to the elft, whilst a larger must go to the right.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # Create a new node if the position is empty
        if node is None:
            return Node(value)
        # Put small values in the left
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        # Put large values in the right
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # Return the node after inserting the new value
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # BST search has the potential to look through less items due to the branching system. 
        # If I wanted to find 70 ina  list with 100 items, I would need to go through 70 to reach it.
        # If a BST has insertions in random order, it could take around only 10 comparisons to reach 70 instead.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # If the value is not in the tree, return false.
        if node is None:
            return False
        # If the value is located, return true.
        if value == node.value:
            return True
        # Determine the size of the search value to determine which subtree to search.
        # If the value is smaller, search left.
        if value < node.value:
            return self._search_recursive(node.left, value)
        # Otherwise, search the right.
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is not None:
            # Visit the left subtree, starting with smaller values
            self._inorder_recursive(node.left, values)
            # Visit the current node
            values.append(node.value)
            # Visit the right subtree, where values get larger
            self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.
    
    print("\n=== TREE CONSTRUCTION ===")

    # Make a new BST
    tree = BST()

    # Set values that be used to create the left and right subtrees
    values = [25, 18, 35, 12, 23, 30, 40]

    # Insert the values into our tree
    # BST reduces search space by moving from left to right to compare values depending on the size of the search value to the current node.
    for value in values:
        tree.insert(value)

    # Show inserted values
    print(f"Values inserted: {values}")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    # In order traversal starts by visiting the left subtree, the current node, and then the right subtree.
    traversal = tree.inorder()
    print(f"In order traversal results: {traversal}")
    

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    # Perform searches for two nodes that exist in our tree
    print(f"Find 12: {tree.search(12)}")
    print(f"Find 30: {tree.search(30)}")

    # Perform searches for two nodes that don't exist in our tree
    print(f"Find 2: {tree.search(2)}")
    print(f"Find 99: {tree.search(99)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    # Duplicate value insertion
    # Since the BST only makes nodes on a system of being smaller or larger, we cannot insert a duplicate node.
    # The duplicate insertion should be ignored.
    tree.insert(12)

    print(f"Attempting to insert duplicate 12 value into the tree: {tree.inorder()}")



if __name__ == "__main__":
    main()