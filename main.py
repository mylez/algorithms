from random import randint

import graph
import priority_queue

adj_list, weights = graph.weighted({
    's': [('a', 2), ('b', 2), ('c', 4)],
    'a': [('c', 2), ('s', 2)],
    'b': [('c', 2), ('s', 2)],
    'c': [('a', 2), ('b', 2), ('d', 1), ('e', 1), ('f', 3), ('s', 4)],
    'd': [('c', 1), ('f', 1)],
    'e': [('c', 1), ('f', 1)],
    'f': [('c', 3), ('d', 1), ('e', 1)]
})

adj_list, weights = graph.weighted({
    'a': [('b', 1), ('e', 10)],
    'b': [('a', 1), ('c', 4)],
    'c': [('b', 4), ('d', 7)],
    'd': [('c', 7), ('e', 2)],
    'e': [('d', 2), ('a', 10)],
})

g = graph.Graph(adj_list, weights)
s = 'a'

print('dijkstra:')
prev, dist = g.dijkstra(s)
for u in g.vertices:
    print(u, prev[u], dist[u])


print('\nmodified:')
prev, dist_w, dist_u = g.dijkstra_modified(s)
for u in g.vertices:
    print(u, prev[u], dist_w[u])

print(g.bfs(s))

