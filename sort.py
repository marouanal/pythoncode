def word_freq(sentence, n):
    words = sentence.split()
    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    sorted_freq = sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))
    return sorted_freq[:n]
 
sentence = "baz bar foo foo zblah zblah zblah baz toto bar"
n = 3
result = word_freq(sentence, n)
print(result)
