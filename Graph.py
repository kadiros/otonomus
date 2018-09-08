import heapq

from Vertex import Vertex


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self):
        return self.previous

    def dijkstra(self, start_id):
        print '''Dijkstra's shortest path'''

        # Init variables
        start = self.get_vertex(start_id)

        # Set the distance for the start node to zero
        start.set_distance(0)

        # Put tuple pair into the priority queue
        unvisited_queue = [(v.get_distance(), v) for v in self]
        heapq.heapify(unvisited_queue)

        while len(unvisited_queue):
            # Pops a vertex with the smallest distance
            uv = heapq.heappop(unvisited_queue)
            current = uv[1]
            current.set_visited()

            # for next in v.adjacent:
            for next_vertex in current.adjacent:
                # if visited, skip
                if next_vertex.visited:
                    continue
                new_dist = current.get_distance() + current.get_weight(next_vertex)

                if new_dist < next_vertex.get_distance():
                    next_vertex.set_distance(new_dist)
                    next_vertex.set_previous(current)
                    print 'updated : current = %s next = %s new_dist = %s' \
                          % (current.get_id(), next_vertex.get_id(), next_vertex.get_distance())
                else:
                    print 'not updated : current = %s next = %s new_dist = %s' \
                          % (current.get_id(), next_vertex.get_id(), next_vertex.get_distance())

            # Rebuild heap
            # 1. Pop every item
            while len(unvisited_queue):
                heapq.heappop(unvisited_queue)
            # 2. Put all vertices not visited into the queue
            unvisited_queue = [(v.get_distance(), v) for v in self if not v.visited]
            heapq.heapify(unvisited_queue)

    def shortest(self, target_id, path=None):
        """ make shortest path from v.previous"""
        v = self.get_vertex(target_id)
        if path is None:
            path = [v.get_id()]

        if v.previous:
            path.append(v.previous.get_id())
            self.shortest(v.previous.get_id(), path)
        return path
