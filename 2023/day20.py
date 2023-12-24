#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/20
"""
from itertools import count
from collections import deque, Counter
import re
import aoc

PUZZLE = aoc.Puzzle(day=20, year=2023)


class Module:
    """Base class for pulse propagation modules"""

    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs.split(", ")
        if "" in self.outputs:
            self.outputs.remove("")
        self.inputs = {}

    def add_input(self, module):
        """Add an input to the module"""

    def process(self, signal, module):
        """Process in input signal from module"""
        # pylint: disable=no-self-use
        del module
        return signal


class FlipFlop(Module):
    """Manage a FlipFlop (%) module"""

    def __init__(self, name, outputs):
        super().__init__(name, outputs)
        self.is_on = False

    def process(self, signal, module):
        del module
        if signal is True:
            return None  # High signals are ignored
        self.is_on = not self.is_on
        return self.is_on


class Conjunction(Module):
    """Manage a Conjunction (&) module"""

    def add_input(self, module):
        self.inputs[module] = False

    def process(self, signal, module):
        self.inputs[module] = signal
        return not all(self.inputs.values())


def load_modules():
    """Load modules from the input data"""
    modules = {}
    for line in PUZZLE.input.splitlines():
        match = re.match(r"([&%])?(\w+) -> (.*)", line)
        type_, name, outputs = match.groups()
        if type_ == "%":
            modules[name] = FlipFlop(name, outputs)
        elif type_ == "&":
            modules[name] = Conjunction(name, outputs)
        else:
            modules[name] = Module(name, outputs)

    new_modules = []
    for source in modules.values():
        for dest in source.outputs:
            if dest not in modules:
                print("Creating dummy module for", dest)
                new_modules.append(Module(dest, ""))
            else:
                modules[dest].add_input(source.name)
    for module in new_modules:
        modules[module.name] = module
    return modules


def solve(part="a"):
    """Solve puzzle"""
    if part == "b":
        return None  # will require alternate approach

    modules = load_modules()

    counter = Counter()
    for round_ in count(1):
        # print("Round", round_+1)
        sent = []
        queue = deque()
        queue.append((False, "button", "broadcaster"))
        while queue:
            signal, source, name = queue.popleft()
            if part == "b" and name == "rx" and signal is False:
                return round_
            # print(f"  {source} -{signal}-> {name}")
            sent.append(signal)
            module = modules[name]
            result = module.process(signal, source)
            if result is None:
                continue  # propagation stopped
            for target in module.outputs:
                queue.append((result, name, target))
        counter.update(sent)
        if part == "a" and round_ == 1000:
            return counter[False] * counter[True]
    return None


if __name__ == "__main__":
    PUZZLE.report_a(solve("a"))
    PUZZLE.report_b(solve("b"))
