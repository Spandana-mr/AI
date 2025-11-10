#Best First Search 

import heapq

def uniform_cost_search_tree(tree, start, goal):
    open_list = []
    closed_list = []
    parent = {start: None}
    cost = {start: 0}

    
    heapq.heappush(open_list, (0, start))

    print(f"\nStarting Uniform Cost Search (Tree) from {start} to {goal}\n")

    while open_list:
        
        print("Open List:", [node for (_, node) in open_list])
        print("Closed List:", closed_list)
        print("\n")

        current_cost, current = heapq.heappop(open_list)
        closed_list.append(current)

        if current == goal:
            print("\nGoal reached!")
            path = []
            node = current
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()

            print("Path:", " -> ".join(path))
            print("Cost to reach goal:", current_cost)
            return

        
        for child, edge_cost in tree.get(current, []):
            total_cost = current_cost + edge_cost
            cost[child] = total_cost
            parent[child] = current
            heapq.heappush(open_list, (total_cost, child))

    print("Goal not found in the tree.")



def take_input():
    tree = {}
    n = int(input("Enter number of edges in the tree: "))

    print("Enter edges in the format: Parent Child Cost")
    for _ in range(n):
        u, v, c = input().split()
        c = int(c)
        tree.setdefault(u, []).append((v, c))  

    start = input("\nEnter start node: ")
    goal = input("Enter goal node: ")

    return tree, start, goal



if __name__ == "__main__":
    tree, start, goal = take_input()
    uniform_cost_search_tree(tree, start, goal)
