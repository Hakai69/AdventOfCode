output = 0
with open("./Day1Input.txt", "r") as file:
    for line in file:
        temp1, temp2 = str(), str()
        for letter in line:
            if letter.isnumeric():
                temp1 = letter
                break
        for letter in line[::-1]:
            if letter.isnumeric():
                temp2 = letter
                break
        output += int(temp1 + temp2)
print(output)