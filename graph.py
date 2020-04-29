import priority_queue


INF = float('infinity')


def weighted(adj_list_w):
    adj_list = {}
    weights = {}

    for u in adj_list_w:
        adj_list[u] = []
        for (v, w) in adj_list_w[u]:
            adj_list[u].append(v)
            weights[(u, v)] = w
    return adj_list, weights


class Graph:

    def __init__(self, adj_list=None, weights=None):

        self.vertices = sorted(adj_list)
        self.adj_list = {u: sorted(adj_list[u]) for u in adj_list}

        if adj_list is None:
            adj_list = {}

        self.weights = weights

    def explore(self, u, count, pre, post, prev, visited):

        visited.add(u)
        pre[u] = count
        count += 1

        for v in self.adj_list[u]:
            if not v in visited:
                prev[v] = u
                count = self.explore(v, count, pre, post, prev, visited)

        post[u] = count
        count += 1

        return count

    def dfs(self):
        count = 1
        pre = {u: -1 for u in self.vertices}
        post = {u: -1 for u in self.vertices}
        prev = {u: None for u in self.vertices}
        visited = set()

        for u in self.vertices:
            if not u in visited:
                self.explore(u, count, pre, post, prev, visited)

        return count, pre, post, visited

    def bfs(self, s):
        dist = {u: INF for u in self.vertices}
        prev = {u: None for u in self.vertices}

        queue = [s]
        visited = {s}
        dist[s] = 0

        while len(queue):
            u = queue.pop(0)
            for v in self.adj_list[u]:
                if not v in visited:
                    visited.add(v)
                    prev[v] = u
                    dist[v] = dist[u] + 1
                    queue.append(v)

        return visited, prev, dist

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
            for v in self.adj_list[u]:
                d_w = self.weights[(u, v)] + dist_w[u]
                d_u = 1 + dist_u[u]
                if (d_w < dist_w[v]) or (d_w == dist_w[v] and d_u < dist_u[v]):
                    dist_w[v] = d_w
                    dist_u[v] = d_u
                    prev[v] = u
                    h.update(v)

        return prev, dist_w, dist_u

    def dijkstra(self, s):
        prev = {u: None for u in self.vertices}
        dist = {u: INF for u in self.vertices}
        dist[s] = 0

        h = priority_queue.PriorityQueue(lambda u, v: dist[u] < dist[v])

        for u in self.vertices:
            h.push(u)

        while h.size():
            u = h.pop()
            for v in self.adj_list[u]:
                w = self.weights[(u, v)] + dist[u]
                if w < dist[v]:
                    dist[v] = w
                    prev[v] = u
                    h.update(v)

        return prev, dist

