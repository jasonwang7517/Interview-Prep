"""
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that 
connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the 
given star graph.
"""

class FindCenterOfStarGraph(object):
    def findCenter(self, edges):
        edgeCounts = {}
        for i in edges:
            if i[1] not in edgeCounts:
                edgeCounts[i[1]] = 1
            else:
                edgeCounts[i[1]] +=  1
            if i[0] not in edgeCounts:
                edgeCounts[i[0]] = 1
            else:
                edgeCounts[i[0]] += 1
        for i in edgeCounts:
            if edgeCounts[i] == len(edges):
                return i
