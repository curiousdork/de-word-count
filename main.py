import re
from map_words import map_words
from shuffle_and_sort import shuffle_words, perform_reduce


# Open the file
with open('story.txt', 'r') as file:
    text = file.read()

words = re.split(r"\W+", text)

# word_mapped = []

# First let us map_words.py
# for word in words:
#     word_mapped.append((word, [1]))
#
# word_mapped.pop()

mapped_words = map_words(words)
shuffled = shuffle_words(mapped_words)
sorted = perform_reduce(shuffled)

for key, value in sorted.items():
    print(key, value)
