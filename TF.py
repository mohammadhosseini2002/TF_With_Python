# Calculate TF in Text With Python

def calculate_tf(word, sentence):
    word_count = sentence.count(word)
    return word_count