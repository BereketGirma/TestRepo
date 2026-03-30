class Statistics_Report:
    def __init__(self, word_freq: dict, total_words: int):
        self.word_freq = word_freq
        self.total_words = total_words
    
    def unique_words_count(self):
        """
        Returns the number of unique words in the text.
        """
        return len(self.word_freq)
    
    def average_word_length(self):
        """
        Returns the average length of words in the text.
        """
        if self.total_words == 0:
            return 0
        total_length = sum(len(word) * count for word, count in self.word_freq.items())
        return total_length / self.total_words

    def longest_word(self):
        """
        Returns the longest word in the text.
        """
        if not self.word_freq:
            return ""

        return max(self.word_freq.keys(), key=len)

    def most_frequent_word(self):
        """
        Returns the most frequent word in the text and its count.
        """
        if not self.word_freq:
            return None, 0
        
        word = max(self.word_freq.items(), key=lambda item: item[1])
        return word
    
    def get_words_starting_with(self, prefix: str):
        """
        Returns a list of words that start with the given prefix.
        """
        prefix = prefix.lower()
        words = [word for word in self.word_freq.keys() if word.startswith(prefix)]
        return sorted(words)

    def get_top_n_words(self, n: int):
        """
        Returns the top n most frequent words and their counts.
        """
        return sorted(self.word_freq.items(), key=lambda item: item[1], reverse=True)[:n]

    def export_report(self, output_file_path: str):
        """Exports the analysis report to a text file."""
        try:
            with open(f"text_document_analyzer/data_output/{output_file_path}", "w", encoding='utf-8') as file:
                file.write("----Text Analysis Report----\n")

                file.write(f"Total Words: {self.total_words}\n")
                file.write(f"Unique Words: {self.unique_words_count()}\n")
                file.write(f"Average Word Length: {self.average_word_length():.2f}\n")
                file.write(f"Longest Word: {self.longest_word()}\n")

                word, count = self.most_frequent_word()
                file.write(f"Most Frequent Word: '{word}' (Count: {count})\n\n")

                file.write("Top 10 words:\n")

                for i, (word, count) in enumerate(self.get_top_n_words(10), 1):
                    file.write(f"{i}. {word} (Count: {count})\n")
        except IOError as e:
            print(f"Error writing report to '{output_file_path}': {e}")