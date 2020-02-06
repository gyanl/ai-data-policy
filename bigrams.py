f = open('text.txt', 'r')

raw = f.read()

text = str(raw).split()

i=1
print("The bigrams are: ")
while i < len(text):
  print(text[i-1] + " - " + text[i])
  i = i+1
