# your code goes here!
class Anagram():
    def __init__(self, word):
        self.word = word
        self.letters = sorted([letter for letter in word])
    
    def match(self, word_list):

        matching_words = []

        for word in word_list:
            if self.letters == sorted([letter for letter in word]):
                matching_words.append(word)
            else:
                return matching_words
