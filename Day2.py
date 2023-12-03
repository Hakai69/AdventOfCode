import re
maximums = {'red': 12, 'green':13, 'blue':14}
gameIdPattern = re.compile(r"[\d]+:")
informationRetriever = re.compile(r"([\d]+ [\w]+)")
informationNumberPattern = re.compile(r"[\d]+")
informationNamePattern = re.compile(r"[a-z]+")
output = 0
with open("./Day2Input.txt", "r") as file:
    for line in file:
        possible = True
        for element in re.findall(informationRetriever, line):
            if maximums[re.search(informationNamePattern, element).group()] < int(re.search(informationNumberPattern, element).group()):
                possible = False
                break
        if possible: output += int(re.search(gameIdPattern, line).group()[:-1])
print(output)