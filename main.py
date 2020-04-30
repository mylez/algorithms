import graph

adj, weights = graph.weighted({
    'a': [('b', 1), ('d', 10)],
    'b': [('c', 1), ('e', 10)],
    'c': [('e', 1)],
    'd': [('e', 1)],
    'e': [],
    's': [('a', 1), ('d', 3)]
})


g = graph.Graph(adj, weights)
best = g.best_shortest_paths('s')

for u in g.vertices:
    print(u, best[u])
