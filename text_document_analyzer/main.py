from services.text_reader import Text_Reader
from services.word_counter import Word_Counter
from services.statistics_report import Statistics_Report

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "report.txt"

    reader = Text_Reader()
    counter = Word_Counter()

    raw_text = reader.read_file(input_file)
    clean_text = reader.normalize_text(raw_text)

    freq = counter.count_words(clean_text)

    report = Statistics_Report(freq, counter.total_words)
    report.export_report(output_file)

    print(f"Analysis report exported to {output_file}")