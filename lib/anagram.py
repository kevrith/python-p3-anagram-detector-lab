class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        target_letters = sorted(self.word)
        matches = []
        for word in word_list:
            if sorted(word.lower()) == target_letters and word.lower() != self.word:
                matches.append(word)
        return matches
