import network
from Graph import Graph

TCP_IP = 'localhost'
port = 12349


def main():
    passenger_info = network.get_info(TCP_IP, port)

    g = Graph(passenger_info)
    print g.get_route()

if __name__ == '__main__':
    main()
