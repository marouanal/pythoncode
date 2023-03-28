#######################################    First Code    #############################################################
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

#######################################    Updated Code    #############################################################

import unittest
from collections import Counter

def word_frequency(sentence, n):
    allwords = sentence.split()
    frequency_list = Counter(allwords)
    sorted_frequency = sorted(frequency_list.items(), key=lambda x: (-x[1], x[0]))
    return sorted_frequency[:n]

class TestWordFrequency(unittest.TestCase):

    def test_word_frequency(self):
        sentence = "baz bar foo foo zblah zblah zblah baz toto bar"
        n = 3
        expected_output = [('zblah', 3), ('bar', 2), ('baz', 2)]
        self.assertEqual(word_frequency(sentence, n), expected_output)

    def test_word_frequency_empty_sentence(self):
        sentence = ""
        n = 3
        expected_output = []
        self.assertEqual(word_frequency(sentence, n), expected_output)

    def test_word_frequency_single_word_sentence(self):
        sentence = "hello"
        n = 1
        expected_output = [('hello', 1)]
        self.assertEqual(word_frequency(sentence, n), expected_output)

    def test_word_frequency_multiple_n(self):
        sentence = "baz bar foo foo zblah zblah zblah baz toto bar"
        n = 5
        expected_output = [('zblah', 3), ('bar', 2), ('baz', 2), ('foo', 2), ('toto', 1)]
        self.assertEqual(word_frequency(sentence, n), expected_output)

    def test_word_frequency_same_frequency(self):
        sentence = "baz bar foo foo zblah zblah zblah baz toto bar toto"
        n = 4
        expected_output = [('zblah', 3), ('bar', 2), ('baz', 2), ('foo', 2)]
        self.assertEqual(word_frequency(sentence, n), expected_output)

if __name__ == '__main__':
    unittest.main()
