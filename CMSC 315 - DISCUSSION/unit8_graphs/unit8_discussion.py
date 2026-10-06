"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """
    # A queue is used here so that BFS can use the current node to reference its neighbors.
    # Once a queued node is searched, it is removed from the queue and added to visited.
    # Nodes that have already been visited in the queue will not be pulled up if not necessary.
    if start not in graph:
        return []
    queue = deque([start])
    visited = {start}
    order = []

    # Neighbors are added to the back of the queue so they can be visited in the next level
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    print("\n=== GRAPH STRUCTURE ===")
    print("TODO: Create and display a graph.")

    # The nodes represent individual quests which may be randomly selected as a starting point.
    # Each edge represents which quests will be potentially unlocked next.
    # Quest 1 can unlock QUest 2 and Quest 3, but not directly Quest 4.
    graph = {
        "Quest 1": ["Quest 2", "Quest 3"],
        "Quest 2": ["Quest 1", "Quest 4", "Quest 5"],
        "Quest 3": ["Quest 1", "Quest 4", "QUest 6"],
        "Quest 4": ["Quest 2", "Quest 3", "Quest 6"],
        "Quest 5": ["Quest 2", "Quest 6"],
        "Quest 6": ["Quest 3", "Quest 4", "Quest 5"],
    }
    print("Quest Linking: ")
    for node, neighbors in graph.items():
        print(f"{node} : {neighbors}")
    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")
    print("TODO: Perform and explain BFS traversal.")

    # BFS takes advantage of our adjacent list by scanning all of its neighbors first for Level 1.
    # The neighbors are then scanned for level 2, and then further on for subsequent levels.
    start = "Quest 4"
    bfs_traversal = bfs(graph, start)
    print(f"Starting Quest: {start}")
    print("BFS searches for nodes starting with the nearest neighbors.")
    print(f"Order, starting from {start}: {bfs_traversal}")

    graph["Quest 7"] = ["Quest 1", "Quest 3"]
    graph["Quest 1"].append("Quest 7")
    print(f"\nNew Quest Added.")
    new_traversal = bfs(graph, start)
    print(f"Updated Quests: {new_traversal}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    print(f"\nEdge Case 1: Missing Start Node")

    missing_start = bfs(graph, "Quest 0")
    print(f"Quest Traversal: {missing_start}")
    print("Since the start node was not present in the list, the result should be empty.")
    
    print(f"\nEdge Case 2: Empty Graph")

    empty_graph = bfs({}, "Quest 1")
    print(f"Quest Traversal: {empty_graph}")
    print("Similarly, an empty list should be returned as there simply is no list.")
if __name__ == "__main__":
    main()