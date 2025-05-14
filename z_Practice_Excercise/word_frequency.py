



def word_frequency(sentence):
    result = {}
    count = 0
    words = sentence.split()
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
        
    most_freq = max(result, key=result.get)

    return most_freq


sentence = "apple banana apple orange banana apple grape"
print(word_frequency(sentence))
