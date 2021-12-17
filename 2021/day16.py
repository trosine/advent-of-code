#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/16
"""
import operator

import aoc

PUZZLE = aoc.Puzzle(day=16, year=2021)


class Packet:
    """Generic type of packet"""

    version = None
    type_id = None
    end_offset = None

    def __init__(self, version, type_id):
        self.version = int(version, 2)
        self.type_id = int(type_id, 2)

    def __str__(self):
        return f'<Packet({self.version}, {self.type_id})>'

    def version_sum(self):
        """Get the sum of this and all child packets"""
        return self.version


class LiteralPacket(Packet):
    """Implementation for literal value packets"""

    value = None

    def __init__(self, version, type_id, value):
        super().__init__(version, type_id)
        self.value = value

    def __str__(self):
        return f'<LiteralPacket({self.version}, {self.type_id}, {self.value})>'

    def get_value(self):
        """Get the value of this packet"""
        return self.value


class OperatorPacket(Packet):
    """Implementation for an operator packet"""

    packets = None
    _operator = {
        0: sum,
        # 1: product (implemented in get_value()
        2: min,
        3: max,
        # 4: literal (implemented in LiteralPacket.get_value()
        5: operator.gt,
        6: operator.lt,
        7: operator.eq,
        }

    def __init__(self, version, type_id):
        super().__init__(version, type_id)
        self.packets = []

    def __str__(self):
        return (
            f'<OperatorPacket({self.version}, '
            f'{self.type_id}, {len(self.packets)})>'
            )

    def version_sum(self):
        """Get the sum of this and all child packets"""
        return self.version + sum(c.version_sum() for c in self.packets)

    def get_value(self):
        """Get the value of this packet"""
        children = (c.get_value() for c in self.packets)
        if self.type_id == 1:
            total = 1
            for child in children:
                total *= child
            return total
        if self.type_id > 4:
            return int(self._operator[self.type_id](*children))
        return self._operator[self.type_id](children)


def parse_packet(packet, offset=0):
    """Parse a packet from the stream"""
    version = packet[offset:offset+3]
    type_id = packet[offset+3:offset+6]

    if type_id == '100':
        chunk_offset = offset + 6
        value = ''
        while True:
            cont = packet[chunk_offset]
            value += packet[chunk_offset+1:chunk_offset+5]
            chunk_offset += 5
            if cont == '0':
                break
        value = int(value, 2)
        result = LiteralPacket(version, type_id, value)
        result.end_offset = chunk_offset
        return result

    length_type = packet[offset+6]
    offset += 7  # skip past version and type_id
    result = OperatorPacket(version, type_id)
    if length_type == '0':
        length = int(packet[offset:offset+15], 2)
        offset += 15  # length_type + 15 bits for length
        result.end_offset = offset + length
        while True:
            child = parse_packet(packet, offset)
            offset = child.end_offset
            result.packets.append(child)
            if child.end_offset >= result.end_offset:
                return result

    length = int(packet[offset:offset+11], 2)
    offset += 11
    while len(result.packets) < length:
        child = parse_packet(packet, offset)
        result.packets.append(child)
        offset = child.end_offset
    result.end_offset = offset
    return result


def solve(part='a'):
    """Solve puzzle"""
    if part == 'a':
        pass
    data = PUZZLE.input
    binary = format(int(data, 16), f'0{4*len(data)}b')
    packet = parse_packet(binary)
    if part == 'a':
        return packet.version_sum()
    return packet.get_value()


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
