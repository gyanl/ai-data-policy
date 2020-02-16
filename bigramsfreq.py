from collections import Counter

## For n most common bigrams
n = 5

result = []
i = 0
j = 0
k = 0

f = open('text.txt', 'r')
raw = f.read()
text = str(raw).split()

print("The bigrams are: ")
while i < len(text)-1:
    result.append(text[i] + "|" + text[i+1])
    i = i+1

sortedresult = sorted(result, key = result.count, reverse = True)

result2 = []

while j < len(sortedresult):
    if sortedresult[j] in result2:
        j = j + 1
    else:
        print(sortedresult[j] , sortedresult.count(sortedresult[j]))
        result2.append(sortedresult[j])
        k = k + 1
        j = j + 1
    if (k >= n):
        break
