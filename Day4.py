import re
winningPattern = re.compile(r": [0-9 ]+")
numbersPattern = re.compile(r"\| [0-9 ]+")

def extractIndex(line: str) -> int | float:
    winningNumbers = [element for element in re.search(winningPattern, line).group()[2:-1].split(" ") if element != ""]
    myNumbers = [element for element in re.search(numbersPattern, line).group()[2:].split(" ") if element != ""]
    
    i = 0
    for number in winningNumbers.copy():
        if number in myNumbers.copy():
            myNumbers.remove(number)
            winningNumbers.remove(number)
            i += 1
    return i if i > 0 else float("-inf")

with open("Day4Input.txt", "r") as file:
    print(round(sum(2**(extractIndex(line)-1) for line in file)))