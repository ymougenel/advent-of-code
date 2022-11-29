#!/usr/bin/env python3
import math
import bisect
import time
import numpy as np
from collections import Counter
import binascii

infos = {}


def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


def transform_hexa_to_binary(hexa_paquet):
    binary_packet = ""
    for i in range(0, len(hexa_paquet)):
        binary = bin(int(hexa_paquet[i], 16))[2:]
        binary_packet += "0" * (4 - len(binary)) + binary
    return binary_packet


def binary_to_digit(binary_string):
    return int(binary_string, 2)


def get_label(bin_paquet):
    return binary_to_digit(bin_paquet[0:3])

def parse_to_array(bin_paquets):
    paquets = []
    reading = "V"
    content = ""
    cur_paquet = []
    for i in range(len(bin_paquets)):
        if reading == "P":
            if i%8 == 0:
                reading = "V"
            else:
                continue

        content += bin_paquets[i]
        # reading Version of type
        if reading == "V" or reading == "T":
            if len(content) == 3:
                cur_paquet.append(binary_to_digit(content))

                if reading == "V":
                    reading = "T"
                else:
                    if cur_paquet[-1] == 4:
                        reading = "M"
                    else:
                        reading = "N"
                content = ""
        # Reading message
        else:
            # Reading type 4 message
            if reading == "M":
                if len(content) == 5:
                    cur_paquet.append(binary_to_digit(content[1:]))
                    keep_reading = content[0] == "1"
                    content = ""
                    if not keep_reading:
                        paquets.append(cur_paquet)
                        cur_paquet = []
                        reading = "P"
            # Reading operators
            else:
                if len(cur_paquet) == 2:
                        cur_paquet.append(int(content))
                        content = ""
                elif len(cur_paquet) == 3:
                    # Leght type Id
                    if cur_paquet[-1] == 0 :
                        if len(content) == 15:
                            cur_paquet.append(binary_to_digit(content))
                            content = ""
                    else:
                        if len(content) == 11:
                            cur_paquet.append(binary_to_digit(content))
                            content = ""

                else:
                    if cur_paquet[2] == 0:
                        if len(content) == cur_paquet[-1]:
                            cur_paquet.append(binary_to_digit(content))
                            paquets.append(cur_paquet)
                            cur_paquet = []
                            content = ""
                            reading = "P"
                    else:
                        if len(content) == cur_paquet[-1]*11:
                            cur_paquet.append(binary_to_digit(content))
                            paquets.append(cur_paquet)
                            cur_paquet = []
                            content = ""
                            reading = "P"

    return  paquets

if __name__ == '__main__':
    start_time = time.time()

    # Init
    hexa_packets = read_file("inputs/part1.example")
    # map = read_file("inputs/my_example")
    hexa_packets = read_file("inputs/part1.input")

    # Part 1
    bin_packets = transform_hexa_to_binary(hexa_packets[0])
    tab = parse_to_array(bin_packets)
    print(tab)
    print(sum([t[0] for t in tab]))

    # Part 2
    print("--- %s seconds ---" % (time.time() - start_time))
