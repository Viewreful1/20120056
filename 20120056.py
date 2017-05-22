#!/usr/bin/env python

import sys

N, M, V = [ int(i) for i in sys.stdin.readline().split() ]

vertex = dict()
for i in range(M):
    a, b = [ int(i) for i in sys.stdin.readline().split() ]

    if not vertex.has_key(a):
        vertex[a] = dict()
    vertex[a][b] = 1

    if not vertex.has_key(b):
        vertex[b] = dict()
    vertex[b][a] = 1

# DFS

visited_edges = list()
edges_to_visit = [ V ]
marked_edges = dict()
while edges_to_visit:
    edge = edges_to_visit.pop()

    if edge in marked_edges:
        continue

    visited_edges.append(edge)
    marked_edges[edge] = 1

    if vertex.has_key(edge):
        edges = sorted(vertex[edge].keys())
        edges = [ edge for edge in edges if edge not in marked_edges ]

        edges_to_visit.extend(reversed(edges))

print ' '.join([ str(i) for i in visited_edges ])

# BFS

visited_edges = list()
edges_to_visit = [ V ]
marked_edges = { V: 1 }
while edges_to_visit:
    edge = edges_to_visit.pop(0)

    visited_edges.append(edge)

    if vertex.has_key(edge):
        edges = sorted(vertex[edge].keys())
        edges = [ edge for edge in edges if edge not in marked_edges]

        for edge in edges:
            marked_edges[edge] = 1
            edges_to_visit.append(edge)

print ' '.join([ str(i) for i in visited_edges ])
