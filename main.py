import re

# Open the file
with open('story.txt', 'r') as file:
    text = file.read()

words = re.split(r"\W+", text)

word_count = {}

# First let us map
for word in words:
    if word in word_count:
        word_count[word].append(1)
    else:
        word_count[word] = [1]

