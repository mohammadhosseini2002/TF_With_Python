# Calculate TF in Text With Python

def calculate_tf(word, sentence):
    word_count = sentence.count(word)
    return word_count

sentence = "This is a Sample is a new book is nice"
word = "is"

tf = calculate_tf(word, sentence)

print(f"The term frequency of '{word}' in the sentence is: {tf}")

#Finish