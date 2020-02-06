f = open('text.txt', 'r')

raw = f.read()

text = str(raw).split()

result = []
freq = []

i=1
print("The bigrams are: ")
while i < len(text):
  if str(text[i-1] + "|" + text[i]) in result:
    freq[i] = freq[i] + 1
  else:
    result.append(str(text[i-1] + "|" + text[i]))
    freq[i] = 1
  i = i+1

print(result)
print(frequency)
