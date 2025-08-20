def soft_Word_in_senteance(sentence):
    words = sentence.split()
    print(words)
    words.sort(key=str.lower)
    print(words)
    sorted_sentence = ' '.join(words)
    return sorted_sentence

sentence = "This is a man world"
sorted_result = soft_Word_in_senteance(sentence)
print("Sorted sentence: ", sorted_result)