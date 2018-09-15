import network
from Graph import Graph
import distance

TCP_IP = '192.168.1.102'
port = 12349


def main():
    passanger_info = network.get_info(TCP_IP, port)
    print passanger_info

    g = Graph()
    g.print_graph()
    g.dijkstra('6')

    print (distance.pnt2line())
    path = g.shortest('4')
    print ('The shortest path : %s' % (path[::-1]))


if __name__ == '__main__':
    main()
