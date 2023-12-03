class Number():
    def __init__(self, value, beginning, line) -> None:
        self.value = value
        self.x0 = beginning
        self.length = len(str(value))
        self.x1 = self.length + beginning - 1
        self.y = line

    def isSurrounded(self, symbols):
        if (self.x0 - 1, self.y) in symbols: return True
        elif (self.x1 + 1, self.y) in symbols: return True
        else:
            for i in range(-1, self.length + 1):
                if (self.x0 + i, self.y - 1) in symbols:
                    return True
                elif (self.x0 + i, self.y + 1) in symbols:
                    return True
        return False

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
            elif letter != "." and letter != "\n" and not letter.isalnum():
                symbols.append((j, i))

symbols = frozenset(symbols)
output = 0
for number in numbers:
    if number.isSurrounded(symbols): output += number.value
print(output)
