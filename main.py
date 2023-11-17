import re
from map_words import map_words
from shuffle_and_sort import shuffle_words, sort_words


# Open the file
with open('story.txt', 'r') as file:
    text = file.read()

words = re.split(r"\W+", text)

word_mapped = []

# First let us map_words.py
for word in words:
    word_mapped.append((word, [1]))

word_mapped.pop()

# Second we do the shuffle and sort phase. all the keys are sorted and grouped
sorted_map = {}

for key, value in word_mapped:
    if key in sorted_map.keys():
        sorted_map[key].append(value[0])
    else:
        sorted_map[key] = value

sorted_map = sorted(sorted_map.items(), key=lambda x: x[1], reverse=True)

# Now let us reduce
reduced_word_map = []

for key, value in sorted_map:
    reduced_word_map.append((key, sum(value)))

for map_reduced_item in reduced_word_map:
    print(map_reduced_item)

