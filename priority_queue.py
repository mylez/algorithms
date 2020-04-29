
def left_index(i):
    return 2*i + 1


def right_index(i):
    return 2*i + 2


def parent_index(i):
    return int((i - 1) / 2)


class PriorityQueue:

    def __init__(self, cmp=lambda a, b: a < b):
        self.array = []
        self.frontier = 0
        self.index = {}
        self.cmp = cmp

    def push(self, a):
        if a in self.index:
            return

        self.adjust_array()

        self.array[self.frontier] = a
        self.index[a] = self.frontier
        self.reheap_up(self.frontier)
        self.frontier += 1

    def pop(self):
        self.frontier -= 1
        a = self.array[0]
        self.swap(0, self.frontier)
        self.array[self.frontier] = None
        del self.index[a]
        self.reheap_down(0)
        return a

    def update(self, a):
        i = self.index[a]
        p_i = parent_index(i)
        l_i = left_index(i)

        if i > 0 and self.cmp(a, self.array[p_i]):
            self.reheap_up(i)

        if l_i < self.frontier:
            ch, ch_i = self.min_child(i)
            if self.cmp(a, ch):
                self.reheap_down(i)

    def reheap_up(self, i):
        while 0 < i:
            p_i = parent_index(i)
            p = self.array[p_i]
            cur = self.array[i]

            if self.cmp(p, cur):
                break

            self.swap(i, p_i)
            i = p_i

    def reheap_down(self, i):
        while left_index(i) < self.frontier:
            cur = self.array[i]
            ch, ch_i = self.min_child(i)

            if self.cmp(cur, ch):
                break

            self.swap(i, ch_i)
            i = ch_i

    def min_child(self, i):
        min_i = left_index(i)
        min = self.array[min_i]

        r_i = right_index(i)
        if r_i < self.frontier and self.cmp(self.array[r_i], min):
            min = self.array[r_i]
            min_i = r_i

        return min, min_i

    def verify(self, i=0):
        l_i = left_index(i)
        r_i = right_index(i)
        for c_i in (l_i, r_i):
            if c_i < self.frontier:
                if self.cmp(self.array[c_i], self.array[i]) \
                        or not self.verify(c_i):
                    return False
        return True

    def swap(self, i, j):
        a = self.array[i]
        b = self.array[j]
        self.array[i] = b
        self.array[j] = a
        self.index[b] = i
        self.index[a] = j

    def adjust_array(self):
        n = len(self.array)
        if self.frontier >= n:
            new_arr = [None,]*(2*n + 1)
        else:
            return
        for i in range(self.frontier):
            new_arr[i] = self.array[i]
        self.array = new_arr

    def size(self):
        return self.frontier

