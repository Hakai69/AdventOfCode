import dataclasses

@dataclasses.dataclass(frozen=True)
class Number():
        value: int
        x: int
        y: int

class Symbol():
    def __init__(self, x, y) -> None:
        self.pos = x, y

    def isSurrounded(self, numbers) -> int | None:
        set1 = set()
        for i in range(3):
            for j in range(3):
                if i == j == 1: continue
                coords = (i + self.pos[0] - 1, j + self.pos[1] - 1)
                if coords in numbers: set1.add(numbers[coords])   
        if len(set1) == 2:
            output = 1
            for number in set1:
                output *= number.value
            return output



numbers: list[Number] = []
symbols: list[tuple] = []
with open("./Day3Input.txt", "r") as file:
    for i, line in enumerate(file):
        counter = 0
        for j, letter in enumerate(line):
            if counter > 0:
                counter -= 1
            elif letter.isnumeric():
                a = [letter]
                for k in range(j + 1, len(line) - 1):
                    nextletter = line[k]
                    if nextletter.isnumeric():
                        a.append(nextletter)
                        counter += 1
                    else: break
                numbers.append(Number(int("".join(a)), j, i))
            elif letter == "*":
                symbols.append(Symbol(j, i))

numbers = {(number.x + i, number.y):number for number in numbers for i in range(len(str(number.value)))}
output = 0
for symbol in symbols:
    temp = symbol.isSurrounded(numbers)
    if temp is not None: output += temp
print(output)
