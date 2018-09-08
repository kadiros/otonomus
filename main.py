from Graph import Graph


def main():
    global print_info, g
    print_info = False
    g = Graph(print_info)

    if print_info:
        g.print_graph()

    g.dijkstra('6')
    # dijkstra calculated all distances from the starting point 1
    path = g.shortest('4')
    print 'The shortest path : %s' % (path[::-1])


if __name__ == '__main__':
    main()
