from collections import deque


class Solution:
    def bfs(self, adj):
        # code here
        # already adjacency list is given
        queue = deque([0])
        visited = set()
        visited.add(0)

        output = []
        while queue:
            # pop the node out of it
            node = queue.popleft()
            output.append(node)

            for neighbour in adj[node]:
                # here adj[node ] is a list again
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        return output
