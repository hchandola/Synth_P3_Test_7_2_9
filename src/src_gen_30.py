from typing import List

def sat309(path: List[int], edges=[[0, 11], [0, 7], [7, 5], [0, 22], [11, 22], [11, 33], [22, 33]], u=0, v=33, bound=3):
    assert path[0] == u and path[-1] == v and all([i, j] in edges for i, j in zip(path, path[1:]))
    return len(path) <= bound
def sol309(edges=[[0, 11], [0, 7], [7, 5], [0, 22], [11, 22], [11, 33], [22, 33]], u=0, v=33, bound=3):
    """Find a path from node u to node v, of a bounded length, in the given digraph on vertices 0, 1,..., n."""
    # Dijkstra's algorithm
    import heapq
    from collections import defaultdict
    queue = [(0, u, u)]  # distance, node, trail

    trails = {}
    neighbors = defaultdict(set)
    for (i, j) in edges:
        neighbors[i].add(j)

    while queue:
        dist, i, j = heapq.heappop(queue)
        if i in trails:
            continue
        trails[i] = j
        if i == v:
            break
        for j in neighbors[i]:
            if j not in trails:
                heapq.heappush(queue, (dist + 1, j, i))
    if v in trails:
        rev_path = [v]
        while rev_path[-1] != u:
            rev_path.append(trails[rev_path[-1]])
        return rev_path[::-1]
# assert sat309(sol309())

