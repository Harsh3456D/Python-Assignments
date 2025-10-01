#input from the user
text = input("Enter text to analyze: ")

#analyzing the text
word_count = len(text.split())
char_count = len(text)
print(f"Word Count: {word_count}")
print(f"Character Count: {char_count}")

#finding the frequency of each word
word_freq = {}
for word in text.split():
    word = word.lower().strip('.,!?;"\'()[]{}')
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
print("Word Frequencies:", word_freq)
