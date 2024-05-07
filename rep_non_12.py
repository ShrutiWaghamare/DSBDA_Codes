paragraph = "This is a sample paragraph with several words. " \
            "We will count the number of words in this paragraph."

# Split the paragraph into words
words = paragraph.split()

# Count the occurrences of each word
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Find repeated and non-repeated words
repeated_words = []
non_repeated_words = []
for word, count in word_counts.items():
    if count > 1:
        repeated_words.append(word)
    else:
        non_repeated_words.append(word)

print("Repeated words:")
for word in repeated_words:
    print(word)

print("\nNon-repeated words:")
for word in non_repeated_words:
    print(word)
