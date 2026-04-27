"""
T4: Chain Traversal

Given a chain (linear graph) with n nodes and n-1 edges, output the traversal
order of nodes starting from either endpoint.

A chain is a graph where:
    - Exactly two nodes have degree 1 (the endpoints)
    - All other nodes have degree 2 (interior nodes)
    - The graph forms a single path with no branches or cycles

The edges are given in arbitrary order. Your task is to determine the chain's
structure and return the nodes in traversal order from one endpoint to the
other. Either direction is accepted as a valid answer.

Example:

    - For n = 5 and edges = [(1, 2), (2, 3), (3, 4), (4, 5)],
      the output should be chain_traversal(n, edges) = [1, 2, 3, 4, 5]
      (or [5, 4, 3, 2, 1]).

      Explanation: The chain is 1 — 2 — 3 — 4 — 5. Starting from endpoint 1
      (a degree-1 node) and walking along the chain produces [1, 2, 3, 4, 5].

    - For n = 4 and edges = [(3, 1), (1, 4), (4, 2)],
      the output should be chain_traversal(n, edges) = [3, 1, 4, 2]
      (or [2, 4, 1, 3]).

      Explanation: Reconstructed, the chain is 3 — 1 — 4 — 2. Endpoints are
      3 and 2 (both degree 1).
"""
from collections import defaultdict
def chain_traversal(n: int, edges: list) -> list:
    degree = [0] * (n+1) # so that it stays 1 indexed
    adjList = defaultdict(list)
    for src, adj in edges:
        degree[src] += 1
        degree[adj] += 1
        adjList[src].append(adj)
        adjList[adj].append(src)
    
    start = -1
    for i, val in enumerate(degree):
        if val == 1:
            start = i
            break
    
    prev = None
    curr = start
    ret = [start]

    for i in range(n - 1): # n-1 iterations 
        visitNext = adjList[curr][0] if adjList[curr][0] != prev else adjList[curr][1] 
        # we go in one way out the other 
        ret.append(visitNext)
        
        prev = curr
        curr = visitNext
    # now we have start 
    return ret

