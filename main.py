import network
from Graph import Graph

TCP_IP = 'localhost'
port = 12349


def main():
    passenger_info = network.get_info(TCP_IP, port)

    g = Graph(passenger_info)
    g.print_graph()
    g.dijkstra('6')

    path = g.shortest('4')
    print ('The shortest path : %s' % (path[::-1]))


if __name__ == '__main__':
    main()
