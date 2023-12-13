import re, math
numberPattern = re.compile(r"[0-9]+")

with open("Day6Input.txt", "r") as file:
    time = int("".join(re.findall(numberPattern, next(file))))
    distance = int("".join(re.findall(numberPattern, next(file))))
    total = math.ceil((time + math.sqrt(time**2 - 4*distance))/2 - 1) - math.floor((time - math.sqrt(time**2 - 4*distance))/2 + 1) + 1

print(total)