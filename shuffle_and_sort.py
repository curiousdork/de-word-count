def shuffle_words(mapped_words):
    shuffled = {}
    for (key,value) in mapped_words:
        if key in shuffled.keys():
            shuffled[key] += value
        else:
            shuffled[key] = value
    return shuffled


def perform_reduce(shuffled_words):
    return dict(sorted(shuffled_words.items(), key=lambda x: x[1], reverse=True))


