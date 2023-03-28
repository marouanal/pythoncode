def word_frequency(sentence, n):
    allwords = sentence.split()
    frequency_list = {}
    for word in allwords:
        if word in frequency_list:
            frequency_list[word] += 1
        else:
            frequency_list[word] = 1
    sorted_frequency = sorted(frequency_list.items(), key=lambda x: (-x[1], x[0]))
    return sorted_frequency[:n]
 
sentence = "baz bar foo foo zblah zblah zblah baz toto bar"
n = 3
result = word_frequency(sentence, n)
print(result)
