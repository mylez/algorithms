import priority_queue


INF = float('infinity')


def weighted(adj_w):
    adj = {}
    weights = {}

    for u in adj_w:
        adj[u] = []
        for (v, w) in adj_w[u]:
            adj[u].append(v)
            weights[(u, v)] = w
    return adj, weights


class Graph:

    def __init__(self, adj=None, weights=None):

        if adj is None:
            adj = {}

        if weights is None:
            weights = {}
            for u in adj:
                for v in adj[u]:
                    weights[(u, v)] = 1

        self.adj = {u: sorted(adj[u]) for u in adj}
        self.weights = weights
        self.vertices = sorted(adj)

    def dfs(self):
        count = 1
        pre = {u: -1 for u in self.vertices}
        post = {u: -1 for u in self.vertices}
        prev = {u: None for u in self.vertices}
        post_order = []

        for u in self.vertices:
            if pre[u] < 0:
                self.explore(u, count, pre, post, prev, post_order)

        return count, pre, post, prev, post_order

    def explore(self, u, count, pre, post, prev, post_order):
        pre[u] = count
        count += 1

        for v in self.adj[u]:
            if pre[v] < 0:
                prev[v] = u
                count = self.explore(v, count, pre, post, prev, post_order)

        post_order.append(u)
        post[u] = count
        count += 1

        return count

    def bfs(self, s):
        dist = {u: INF for u in self.vertices}
        prev = {u: None for u in self.vertices}

        queue = [s]
        visited = {s}
        dist[s] = 0

        while len(queue):
            u = queue.pop(0)
            for v in self.adj[u]:
                if not v in visited:
                    visited.add(v)
                    prev[v] = u
                    dist[v] = dist[u] + 1
                    queue.append(v)

        return visited, prev, dist

    def dijkstra(self, s):
        prev = {u: None for u in self.vertices}
        dist = {u: INF for u in self.vertices}
        dist[s] = 0

        h = priority_queue.PriorityQueue(lambda u, v: dist[u] < dist[v])

        for u in self.vertices:
            h.push(u)

        while h.size():
            u = h.pop()
            for v in self.adj[u]:
                w = self.weights[(u, v)] + dist[u]
                if w < dist[v]:
                    dist[v] = w
                    prev[v] = u
                    h.update(v)

        return prev, dist

    def dijkstra_modified(self, s):
        prev = {u: None for u in self.vertices}
        dist_w = {u: INF for u in self.vertices}
        dist_u = {u: INF for u in self.vertices}

        dist_w[s] = 0
        dist_u[s] = 0

        def u_lt_v(u, v):
            if dist_w[u] == dist_w[v]:
                return dist_u[u] < dist_u[v]
            return dist_w[u] < dist_w[v]

        h = priority_queue.PriorityQueue(u_lt_v)

        for u in self.vertices:
            h.push(u)

        while h.size():
            u = h.pop()
            for v in self.adj[u]:
                d_w = self.weights[(u, v)] + dist_w[u]
                d_u = 1 + dist_u[u]
                if (d_w < dist_w[v]) or (d_w == dist_w[v] and d_u < dist_u[v]):
                    dist_w[v] = d_w
                    dist_u[v] = d_u
                    prev[v] = u
                    h.update(v)

        return prev, dist_w, dist_u

    def decompose(self):
        _, _, _, _, post_order = self.reverse().dfs()
        pre = {u: -1 for u in self.vertices}
        components = []

        for u in reversed(post_order):
            if pre[u] < 0:
                explored = []
                self.explore(u, 1, pre, {}, {}, explored)
                components.append(sorted(explored))

        return components

    def reverse(self):
        adj = {u: [] for u in self.vertices}
        weights = {(v, u): self.weights[(u, v)] for (u, v) in self.weights}

        for u in self.vertices:
            for v in self.adj[u]:
                adj[v].append(u)

        return Graph(adj, weights)