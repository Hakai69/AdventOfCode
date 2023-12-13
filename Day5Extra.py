import re, functools
numberPattern = re.compile(r"[0-9]+")

@functools.total_ordering
class Interval:
    def __init__(self, bottom, top) -> None:
        self.bottom = bottom
        self.top = top
    
    def __add__(self, number: int):
        return Interval(self.bottom + number, self.top + number)
    def __sub__(self, number: int):
        return Interval(self.bottom - number, self.top - number)
    
    def __contains__(self, coord) -> None:
        return self.bottom <= coord < self.top
    
    def intersect(self, other: object):
        return not (self.bottom >= other.top or self.top <= other.bottom)

    def intersection(self, other: object):
        if not self.intersect(other): return [self]
        divisions = []
        divisions.append(self.bottom)
        if other.bottom in self and other.bottom != self.bottom: divisions.append(other.bottom)
        if other.top in self: divisions.append(other.top)
        divisions.append(self.top)
        return [Interval(divisions[i], divisions[i+1]) for i in range(len(divisions) - 1)]
    
    def __eq__(self, other: object) -> bool:
        return self.bottom == other.bottom and self.top == other.top

    def __hash__(self) -> int:
        return hash(str(self))
    
    def __str__(self) -> str:
        return f"({self.bottom}-{self.top})"
    
    def __lt__(self, other) -> bool:
        return self.bottom < other.bottom
    
    # def __eq__(self, other: object) -> bool:
    #     return self.bottom == other.bottom
    
dictionaries: list[dict] = list()
seeds: list[int] = list()
with open("Day5Input.txt", "r") as file:
    seeds = [Interval(int(string.split(" ")[0]), int(string.split(" ")[0]) + int(string.split(" ")[1])) for string in re.findall(r"[0-9]+ [0-9]+", next(file).split(":")[1])]
    for line in file:
        if line[0].isalpha():
            dictionary = {}
            for line in file:
                if line[0] == "\n": break
                numbers = [int(element) for element in re.findall(numberPattern, line)]
                dictionary[Interval(numbers[1], numbers[1] + numbers[2])] = numbers[0]
            dictionaries.append(dictionary)

tracker: list[int] = list()
for seed in seeds:
    intervals = [seed]
    for dictionary in dictionaries:
        newintervals = intervals.copy()
        for limits, distance in dictionary.items():
            pendingRemove = []
            for jnterval in intervals:
                if jnterval.intersect(limits):
                    for fragment in jnterval.intersection(limits):
                        if fragment.intersect(limits):
                            newintervals.append(fragment + distance - limits.bottom)
                            pendingRemove.append(jnterval)
                        else: 
                            intervals.append(fragment)
                            newintervals.append(fragment)

            for jnterval in pendingRemove:
                if jnterval in newintervals:
                    newintervals.remove(jnterval)       
                    intervals.remove(jnterval) 
            
        intervals = newintervals.copy()
    tracker.append(min(intervals))
print("Minimum location: ", min(tracker).bottom)