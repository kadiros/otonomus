import heapq
from sets import Set

import distance
import logger
from Vertex import Vertex

MAX_PASSENGER_DISTANCE = 200


class Graph:
    def __init__(self, passenger_info):
        self.passenger_info = passenger_info
        self.vert_dict = {}
        self.pick_up_set = Set()
        self.drop_loc_set = Set()
        self.num_vertices = 0
        self.read_vertices_from_file()
        self.read_edges_from_file()

    def __iter__(self):
        return iter(self.vert_dict.values())

    def read_vertices_from_file(self):
        vertices = open("coor.txt", "r")

        if vertices.mode == "r":
            contents = vertices.read()
            self.add_vertices(contents.splitlines())
            logger.log(contents)

        vertices.close()

    def read_edges_from_file(self):
        edges = open("edges.txt", "r")
        if edges.mode == "r":
            contents = edges.read()
            self.add_edges(contents.splitlines())
            logger.log(contents)
        edges.close()

    def add_vertices(self, lines):
        for line in lines:
            self.add_vertex(line)

    def add_vertex(self, node):
        node = node.split(" ")
        self.num_vertices += 1
        new_vertex = Vertex(node[0], int(node[1]), int(node[2]))
        self.vert_dict[node[0]] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edges(self, lines):
        for line in lines:
            raw = line.split(" ")
            if len(raw) > 3:
                self.add_edge(raw[0], raw[1], raw[2], raw[3])
            else:
                self.add_edge(raw[0], raw[1], raw[2])

    def add_edge(self, frm, to, cost=0, is_two_way=False):
        cost = int(cost)
        self.add_edge_internal(cost, frm, to)
        if is_two_way:
            self.add_edge_internal(cost, to, frm)

    def add_edge_internal(self, cost, frm, to):
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.add_possible_terminal_edge(frm, to)

    def add_possible_terminal_edge(self, frm, to):
        p = self.passenger_info[0][1], self.passenger_info[0][2]
        d = self.passenger_info[1][1], self.passenger_info[1][2]
        f = self.get_vertex(frm)
        t = self.get_vertex(to)

        if p is None or d is None or f is None or t is None:
            return

        # is possible pick up location
        if self.is_near(p, f, t):
            self.pick_up_set.add((frm, to))

        # is possible drop down location
        if self.is_near(d, f, t):
            self.drop_loc_set.add((frm, to))

    def is_near(self, p, s, e):
        return distance.pnt2line(p, (s.x, s.y), (e.x, e.y))[0] < MAX_PASSENGER_DISTANCE

    def get_vertices(self):
        return self.vert_dict.keys()

    def get_route(self):
        route = None
        for p in self.pick_up_set:
            for d in self.drop_loc_set:
                r = self.get_route_internal(p, d)
                if r is None:
                    continue
                if route is None or r[0] < route[0]:
                    route = r

        logger.log(route)
        return route

    def get_route_internal(self, p, d):
        sp = self.get_shortest_path('1', p[0])

        p0 = self.get_vertex(p[0])
        cost = p0.distance

        cost += p0.get_weight(self.get_vertex(p[1]))

        pd = self.get_shortest_path(p[1], d[0])
        d0 = self.get_vertex(d[0])
        cost += d0.distance

        cost += d0.get_weight(self.get_vertex(d[1]))

        df = self.get_shortest_path(d[1], '1')
        cost += self.get_vertex('1').distance

        lsp = len(sp)
        lpd = len(pd)
        ldf = len(df)
        if lsp > 1 and sp[lsp - 2] is pd[0] \
                or lpd > 1 and pd[lpd - 2] is df[0] \
                or lpd > 1 and sp[lsp - 1] is pd[1] \
                or ldf > 1 and pd[lpd - 1] is df[1]:
            return None

        return cost, sp + pd + df

    def get_shortest_path(self, start_id, target_id):
        self.dijkstra(start_id)
        return self.shortest(target_id)[::-1]

    def dijkstra(self, start_id):
        logger.log("Dijkstra's shortest path")
        for v in self:
            v.reset()
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
                    logger.log('updated : current = %s next = %s new_dist = %s' \
                               % (current.get_id(), next_vertex.get_id(), next_vertex.get_distance()))
                else:
                    logger.log('not updated : current = %s next = %s new_dist = %s' \
                               % (current.get_id(), next_vertex.get_id(), next_vertex.get_distance()))

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

    def print_graph(self):
        logger.log('Graph data:')
        for v in self:
            for w in v.get_connections():
                vid = v.get_id()
                wid = w.get_id()
                logger.log('( %s , %s, %3d)' % (vid, wid, v.get_weight(w)))
