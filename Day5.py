import re
numberPattern = re.compile(r"[0-9]+")

dictionaries: list[dict] = list()
seeds: list[int] = list()
with open("Day5Input.txt", "r") as file:
    seeds = [int(element) for element in next(file).split(" ")[1:]]
    for line in file:
        if line[0].isalpha():
            dictionary = {}
            for line in file:
                if line[0] == "\n": break
                numbers = [int(element) for element in re.findall(numberPattern, line)]
                dictionary[(numbers[1], numbers[1] + numbers[2])] = numbers[0]
            dictionaries.append(dictionary)

tracker: list[int] = list()
for seed in seeds:
    for dictionary in dictionaries:
        temp = seed
        for key, value in dictionary.items():
            if key[0] <= seed < key[1]:
                temp = value + seed - key[0]
        seed = temp
    tracker.append(seed)
print(min(tracker))