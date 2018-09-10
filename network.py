import socket
import struct

import logger


def get_info(ip, port):
    global s, my_bytes
    s = socket.socket()
    s.connect((ip, port))
    data = s.recv(1024)
    s.close()
    my_bytes = bytearray(data)
    l1 = get_location(my_bytes, 0)
    l2 = get_location(my_bytes, 11)
    return l1, l2


def get_location(my_bytes, offset):
    if my_bytes[offset] == my_bytes[offset + 1] == 255:
        is_pick_up = my_bytes[offset + 2] == 0
        x_coor = struct.unpack("<L", my_bytes[offset + 3:offset + 7])[0]
        y_coor = struct.unpack("<L", my_bytes[offset + 7:offset + 11])[0]
        logger.log(("is pick-up: ", is_pick_up))
        logger.log(("x: ", x_coor))
        logger.log(("y: ", y_coor))
        return is_pick_up, x_coor, y_coor
