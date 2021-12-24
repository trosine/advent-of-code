#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/23
"""
import collections
import re

import aoc

PUZZLE = aoc.Puzzle(day=23, year=2021)
ROOM_OFFSETS = 'ABCD'
ROOM_ENTRANCES = (2, 4, 6, 8)


class State(collections.namedtuple('StateT', ['hall', 'rooms'])):
    """Represents the current state of the burrow"""

    def hall_to_room_moves(self):
        """All possible moves from the hallway to their final room"""
        hall_pods = [
            (kind, pos)
            for pos, kind in enumerate(self.hall)
            if kind != '.'
            ]
        for kind, pos in hall_pods:
            room_offset = ROOM_OFFSETS.index(kind)
            entrance = ROOM_ENTRANCES[room_offset]
            room = self.rooms[room_offset]
            start, end = sorted((pos, entrance))
            if self.hall[start+1:end] != '.' * (end - start - 1):
                # path blocked by another amphipod
                continue
            if re.match(r'\.+' + kind + '*$', room):
                depth = room.rindex('.')  # how deep into the room to go
                new_hall = replace_char(self.hall, pos, '.')
                new_room = replace_char(room, depth, kind)
                new_rooms = replace_item(self.rooms, room_offset, new_room)
                # steps to the entrance, 1 step into room, 1 room depth
                cost = end - start + 1 + depth
                cost *= 10 ** room_offset
                yield cost, State(''.join(new_hall), new_rooms)
                continue

    def room_to_hall_moves(self):
        """Find moves from rooms into the hall"""
        for room_offset, room in enumerate(self.rooms):
            room_kind = ROOM_OFFSETS[room_offset]
            entrance = ROOM_ENTRANCES[room_offset]
            if room in (room_kind * 2, f'.{room_kind}'):
                continue  # already complete
            for depth, kind in enumerate(room):
                if kind == '.':
                    continue  # empty space, nothing to move
                # print(f'{kind} can move from room[{room_offset}][{depth}]')
                for hall_pos, current in enumerate(self.hall):
                    if current != '.':
                        continue  # already occupied
                    if hall_pos in ROOM_ENTRANCES:
                        continue  # cannot block rooms
                    start, end = sorted((entrance, hall_pos))
                    if self.hall[start+1:end] != '.' * (end - start - 1):
                        continue  # path blocked
                    new_hall = replace_char(self.hall, hall_pos, kind)
                    new_room = replace_char(room, depth, '.')
                    new_rooms = replace_item(self.rooms, room_offset, new_room)
                    # steps to the entrance, 1 step into room, 1 room depth
                    cost = end - start + 1 + depth
                    cost *= 10 ** ROOM_OFFSETS.index(kind)
                    yield cost, State(new_hall, new_rooms)
                break  # deeper amphipods are blocked

    def moves(self):
        """All possible moves"""
        moved_to_room = False
        for state in self.hall_to_room_moves():
            yield state
            moved_to_room = True
        if moved_to_room:
            return
        yield from self.room_to_hall_moves()


def replace_char(string, index, char):
    """Replace the character at index with char"""
    return ''.join((
        string[:index],
        char,
        string[index+1:],
        ))


def replace_item(sequence, index, replacement):
    """Replace the item at index with replacement"""
    new = list(sequence)
    new[index] = replacement
    return tuple(new)


def search(state):
    """Search for the lowest cost solution"""
    room_len = len(state.rooms[0])
    end_state = tuple(
        kind * room_len
        for kind in ROOM_OFFSETS
        )
    queue = collections.deque([state])
    seen = {state: 0}
    finished = 0
    best = float('inf')
    rounds = 0
    while queue:
        rounds += 1
        if rounds % 10000 == 0:
            print(f'{rounds}: q={len(queue)} f={finished}, b={best}', end='\r')
        current = queue.popleft()
        for new_state in current.moves():
            new_cost = seen[current] + new_state[0]
            new_state = new_state[1]
            if new_state in seen and new_cost >= seen[new_state]:
                continue  # already seen this with a better cost
            seen[new_state] = new_cost
            if new_state.rooms == end_state:
                finished += 1
                best = min(best, new_cost)
            elif new_cost < best:
                queue.append(new_state)
    print(f'\n{rounds}: fin={finished}, best={best}')
    return best


def solve(part='a'):
    """Solve puzzle"""
    rooms = [''] * 4
    data = PUZZLE.input.splitlines()
    if part == 'b':
        data.insert(3, '#D#C#B#A#')
        data.insert(4, '#D#B#A#C#')
    findall = re.findall(r'[.A-D]+', '\n'.join(data))
    hallway = findall.pop(0)
    for pos, amphipod in enumerate(findall):
        rooms[pos % 4] += amphipod
    state = State(hallway, tuple(rooms))
    print(state)
    return search(state)


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
