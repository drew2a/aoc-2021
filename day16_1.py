import sys
from pathlib import Path
from typing import List

from bitstring import BitArray

inputs = BitArray(hex=Path(sys.argv[1]).read_text().strip()).bin


def read_literal(packet):
    if not packet:
        return None
    literals = []
    for i in range(0, len(packet), 5):
        literals.append(packet[i + 1:i + 5])
        if packet[i] == '0':
            break
    literal = ''.join(literals)
    return int(literal, 2), len(literal) + len(literals)


def split(packet, number):
    return packet[:number], packet[number:]


def read_packet(packet: List):
    version, packet = split(packet, 3)
    type_id, packet = split(packet, 3)

    if not version or not type_id:
        return None
    version = int(version, 2)

    if int(type_id, 2) == 4:  # letter
        literal, literal_length = read_literal(packet)
        return version, literal, literal_length + 6
    else:  # operator
        length_type_id = packet[0]
        packet = packet[1:]
        if length_type_id == '0':
            total_length_in_bits, packet = split(packet, 15)
            packet = packet[:int(total_length_in_bits, 2)]
            values = []
            shift = 0
            while sub_packet := read_packet(packet[shift:]):
                version += sub_packet[0]
                values.append(sub_packet[1])
                shift += sub_packet[2]
            return version, values, len(packet) + 15 + 1 + 6
        else:
            number_of_sub_packets, packet = split(packet, 11)
            length = 0
            values = []
            for _ in range(int(number_of_sub_packets, 2)):
                sub_packet = read_packet(packet)
                version += sub_packet[0]
                values.append(sub_packet[1])
                length += sub_packet[2]
                packet = packet[sub_packet[2]:]
            return version, values, length + 11 + 1 + 6


print(read_packet(inputs))
