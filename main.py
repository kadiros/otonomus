import heapq

from Graph import Graph


def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return


def dijkstra(aGraph, start, target):
    print '''Dijkstra's shortest path'''
    # Set the distance for the start node to zero
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(), v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        # for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                print 'updated : current = %s next = %s new_dist = %s' \
                      % (current.get_id(), next.get_id(), next.get_distance())
            else:
                print 'not updated : current = %s next = %s new_dist = %s' \
                      % (current.get_id(), next.get_id(), next.get_distance())

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(), v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)


if __name__ == '__main__':

    g = Graph()

    g.add_vertex('1')
    g.add_vertex('2')
    g.add_vertex('3')
    g.add_vertex('4')
    g.add_vertex('5')
    g.add_vertex('6')
    g.add_vertex('7')
    g.add_vertex('8')
    g.add_vertex('9')
    g.add_vertex('10')
    g.add_vertex('11')
    g.add_vertex('12')
    g.add_vertex('13')
    g.add_vertex('14')
    g.add_vertex('15')
    g.add_vertex('16')
    g.add_vertex('17')
    g.add_vertex('18')
    g.add_vertex('19')
    g.add_vertex('20')
    g.add_vertex('21')
    g.add_vertex('22')
    g.add_vertex('23')
    g.add_vertex('24')
    g.add_vertex('25')
    g.add_vertex('26')
    g.add_vertex('27')
    g.add_vertex('28')
    g.add_vertex('29')
    g.add_vertex('30')
    g.add_vertex('31')
    g.add_vertex('32')
    g.add_vertex('33')
    g.add_vertex('34')
    g.add_vertex('35')
    g.add_vertex('36')
    g.add_vertex('37')
    g.add_vertex('38')
    g.add_vertex('39')
    g.add_vertex('40')
    g.add_vertex('41')
    g.add_vertex('42')
    g.add_vertex('43')
    g.add_vertex('44')

    g.add_edge('1', '2', 86)
    g.add_edge('1', '3', 37)
    g.add_edge('3', '5', 60)
    g.add_edge('3', '4', 52)
    g.add_edge('2', '6', 76)
    g.add_edge('2', '4', 63)
    g.add_edge('4', '5', 49)
    g.add_edge('6', '7', 23)
    g.add_edge('7', '8', 23)
    g.add_edge('8', '9', 38)
    g.add_edge('4', '9', 73)
    g.add_edge('6', '10', 110)
    g.add_edge('10', '11', 55)
    g.add_edge('11', '12', 14)
    g.add_edge('12', '13', 15)
    g.add_edge('13', '14', 19)
    g.add_edge('14', '15', 43)
    g.add_edge('7', '12', 107)
    g.add_edge('8', '14', 95)
    g.add_edge('9', '15', 86)
    g.add_edge('15', '16', 32)
    g.add_edge('16', '17', 112)
    g.add_edge('5', '17', 104)
    g.add_edge('10', '18', 55)
    g.add_edge('18', '19', 37)
    g.add_edge('19', '20', 48)
    g.add_edge('20', '24', 53)
    g.add_edge('24', '25', 34)
    g.add_edge('25', '26', 78)
    g.add_edge('26', '30', 88)
    g.add_edge('30', '31', 93)
    g.add_edge('11', '19', 53)
    g.add_edge('13', '21', 19)
    g.add_edge('21', '20', 44)
    g.add_edge('21', '22', 54)
    g.add_edge('22', '24', 44)
    g.add_edge('22', '23', 23)
    g.add_edge('15', '23', 32)
    g.add_edge('23', '25', 68)
    g.add_edge('16', '27', 125)
    g.add_edge('27', '26', 26)
    g.add_edge('27', '28', 94)
    g.add_edge('28', '29', 45)
    g.add_edge('28', '30', 45)
    g.add_edge('17', '29', 181)
    g.add_edge('29', '31', 57)
    g.add_edge('18', '32', 61)
    g.add_edge('32', '34', 37)
    g.add_edge('34', '36', 29)
    g.add_edge('36', '37', 65)
    g.add_edge('20', '33', 63)
    g.add_edge('33', '35', 45)
    g.add_edge('32', '33', 71)
    g.add_edge('34', '35', 59)
    g.add_edge('36', '35', 77)
    g.add_edge('37', '38', 21)
    g.add_edge('20', '38', 218)
    g.add_edge('38', '39', 49)
    g.add_edge('39', '40', 56)
    g.add_edge('40', '41', 43)
    g.add_edge('26', '41', 299)
    g.add_edge('37', '42', 114)
    g.add_edge('42', '43', 32)
    g.add_edge('43', '44', 43)
    g.add_edge('39', '42', 63)
    g.add_edge('40', '43', 59)
    g.add_edge('41', '44', 60)
    g.add_edge('31', '44', 960)

    print 'Graph data:'
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print '( %s , %s, %3d)' % (vid, wid, v.get_weight(w))

    dijkstra(g, g.get_vertex('1'), g.get_vertex('26'))

    target = g.get_vertex('26')
    path = [target.get_id()]
    shortest(target, path)
    print 'The shortest path : %s' % (path[::-1])
