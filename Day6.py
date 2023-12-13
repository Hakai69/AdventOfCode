import re, math
numberPattern = re.compile(r"[0-9]+")

with open("Day6Input.txt", "r") as file:
    times = re.findall(numberPattern, next(file))
    distances = re.findall(numberPattern, next(file))

    total = 1
    for time, distance in zip(times, distances):
        time, distance = int(time), int(distance)
        total *= math.ceil((time + math.sqrt(time**2 - 4*distance))/2 - 1) - math.floor((time - math.sqrt(time**2 - 4*distance))/2 + 1) + 1

print(total)

    