import re
stringToNum = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
temp = '|'.join(stringToNum)
pattern = re.compile('\d|' + temp)
reversedpattern = re.compile('\d|' + temp[::-1])
output = 0
with open("./Day1Input.txt", "r") as file:
    for line in file:
        temp1, temp2 = str(), str()
        temp1 = re.search(pattern, line).group()
        if temp1 in stringToNum: temp1 = stringToNum[temp1]
        temp2 = re.search(reversedpattern, line[::-1]).group()
        if isinstance(temp2, str): temp2 = temp2[::-1]
        if temp2 in stringToNum: temp2 = stringToNum[temp2]
        output += int(temp1)*10 + int(temp2)
print(output)