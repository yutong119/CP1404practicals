"""
Word Occurrences
Estimate: 25 minutes
Actual:   35 minutes
"""
text = input("Text: ")
words = text.split()

words_counts = {}
for word in words:
    if word in words_counts:
        words_counts[word] += 1
    else:
        words_counts[word] = 1

max_length = 0
for word in words_counts:
    if len(word) > max_length:
        max_length = len(word)

for word in sorted(words_counts.keys()):
    print(f"{word:{max_length}} = {words_counts[word]}")

