from collections import defaultdict

class Word_Counter:
    STOP_WORDS = {
        "the", "and", "is", "at", "which", "on", "a", "an", "as",
        "are", "was", "were", "been", "be", "have", "has", "had", 
        "do", "does", "did"
    }

    def __init__(self):
        self.word_freq = defaultdict(int)
        self.total_words = 0

    def count_words(self, text: str):
        words = text.split()

        for word in words:
            if len(word) < 3:
                continue

            if word in self.STOP_WORDS:
                continue

            self.word_freq[word] += 1
            self.total_words += 1
        return self.word_freq