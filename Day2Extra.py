import re
gameIdPattern = re.compile(r"[\d]+:")
informationRetriever = re.compile(r"([\d]+ [\w]+)")
informationNumberPattern = re.compile(r"[\d]+")
informationNamePattern = re.compile(r"[a-z]+")
output = 0
with open("./Day2Input.txt", "r") as file:
    for line in file:
        minimum = dict()
        for element in re.findall(informationRetriever, line):
            color = re.search(informationNamePattern, element).group()
            number = int(re.search(informationNumberPattern, element).group())
            if number > minimum.get(color, 0):
                minimum[color] = number
        output += minimum.get('red', 0) * minimum.get('green', 0) * minimum.get('blue', 0)
print(output)