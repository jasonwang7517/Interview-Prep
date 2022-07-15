"""
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer 
array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, 
and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise. 
"""

from collections import defaultdict

class FindIfPathExistsInInGraph(object):
    def validPath(self, n, edges, source, destination):
        if source == destination:
            return True
        paths = defaultdict(list)
        for i in edges:
            paths[i[0]].append(i[1])
            paths[i[1]].append(i[0])
        
        visited = [False] * n
        q = []
        q.append(source)
        visited[source] = True
        while q:
            current = q.pop(0)                
            for i in paths[current]:
                if i == destination:
                    return True
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
        return False