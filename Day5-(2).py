from collections import Counter

file = open("sparkout-internship/sample.txt", "r")

text = file.read()

words = text.lower().split()

count = Counter(words)

print("Word Frequency:")

for word, frequency in count.items():
    print(word, ":", frequency)

file.close()