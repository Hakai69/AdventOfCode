class Hand():
    cards = [2,3,4,5,6,7,8,9,'T','J','Q','K','A']
    hierarchy = {str(key):value for key, value in zip(cards, range(len(cards)))}

    def __init__(self, value: str) -> None:
        self.value = value
    
    def __eq__(self, other: object) -> bool:
        return self.value == other.value
    def __hash__(self) -> int:
        return hash(self.value)
    def __lt__(self, other: object) -> bool:
        xdict, ydict = dict(), dict()
        for i in self.value:
            if i in xdict: xdict[i] += 1
            else: xdict[i] = 1
        for i in other.value:
            if i in ydict: ydict[i] += 1
            else: ydict[i] = 1

        for i, j in zip(sorted(xdict.values(), reverse=True), sorted(ydict.values(),reverse=True)):
            if i == j: continue
            else: return i < j
        for i, j in zip(self.value, other.value):
            if i == j: continue
            else: return Hand.hierarchy[i] < Hand.hierarchy[j]
        raise Exception("WTF, they're supposed to be different hands.")
    def __str__(self) -> str:
        return self.value

dictionary = dict()
with open("Day7Input.txt", "r") as file:
    dictionary = {Hand(line[:5]):int(line[5:]) for line in file}

total = 0
for i, hand in enumerate(sorted(dictionary.keys())):
    total += (i+1) * dictionary[hand]
print(total)



        
    