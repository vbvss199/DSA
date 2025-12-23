import heapq


class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # build the adjacency list which consists the edge and distance
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))  # important

        # priorityqueue
        heap = []
        # create a distance array
        distance = [float("inf")] * V
        # at the start we need to push(0,srcnode)
        distance[src] = 0
        heapq.heappush(heap, (0, src))

        # now iterate the heapq
        while heap:
            dist, node = heapq.heappop(heap)
            if dist > distance[node]:
                continue
            # now go to the adjacency list and compare
            for neighbournode, weight in adj[node]:
                # now we need to calculate the current distance which is dist and the edgeWeight
                if dist + weight < distance[neighbournode]:
                    distance[neighbournode] = dist + weight
                    heapq.heappush(heap, (distance[neighbournode], neighbournode))

        return distance
