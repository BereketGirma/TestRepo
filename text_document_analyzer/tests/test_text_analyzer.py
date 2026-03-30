"""Pytest suite for Text Document Analyzer challenge requirements (Challenge 1 scope for this module)."""

from pathlib import Path

from services.statistics_report import Statistics_Report
from services.text_reader import Text_Reader
from services.word_counter import Word_Counter


def test_read_file_returns_text_for_existing_file():
    """Reads a file from data_input and returns its text content."""
    reader = Text_Reader()

    fixture_path = Path("text_document_analyzer/data_input/test_read_fixture.txt")
    fixture_text = "Reading fixture content for analyzer test."
    fixture_path.write_text(fixture_text, encoding="utf-8")

    try:
        assert reader.read_file("test_read_fixture.txt") == fixture_text
    finally:
        fixture_path.unlink(missing_ok=True)


def test_read_file_missing_file_returns_none():
    """Returns None when input file does not exist."""
    reader = Text_Reader()
    assert reader.read_file("definitely_missing_file.txt") is None


def test_normalize_text_handles_none_and_returns_empty_string():
    """Converts None input to empty normalized text."""
    reader = Text_Reader()
    assert reader.normalize_text(None) == ""


def test_normalize_text_lowercases_strips_punctuation_and_collapses_spaces():
    """Normalizes casing, punctuation, and whitespace while preserving numbers."""
    reader = Text_Reader()
    raw = "  Hello, WORLD!! 2026...\nThis\tis   A-Test.  "
    normalized = reader.normalize_text(raw)
    assert normalized == "hello world 2026 this is atest"


def test_count_words_excludes_stop_words_and_words_shorter_than_three_chars():
    """Ignores stop words and short tokens, then counts only valid words."""
    reader = Text_Reader()
    counter = Word_Counter()
    text = "the and is at be an to go app APP apple banana apple 42"

    # Match production flow: normalize first so casing and punctuation are standardized.
    freq = counter.count_words(reader.normalize_text(text))

    assert dict(freq) == {"app": 2, "apple": 2, "banana": 1}
    assert counter.total_words == 5


def test_count_words_empty_text_results_in_zero_counts():
    """Produces no frequencies and zero total words for empty text."""
    counter = Word_Counter()

    freq = counter.count_words("")

    assert dict(freq) == {}
    assert counter.total_words == 0


def test_statistics_for_empty_frequency_map_match_expected_defaults():
    """Returns documented default statistics for no analyzed words."""
    report = Statistics_Report({}, 0)

    assert report.unique_words_count() == 0
    assert report.average_word_length() == 0
    assert report.longest_word() == ""
    assert report.most_frequent_word() == (None, 0)
    assert report.get_top_n_words(10) == []
    assert report.get_words_starting_with("ab") == []


def test_average_length_longest_and_most_frequent_with_real_counts():
    """Computes aggregate statistics correctly from non-empty counts."""
    freq = {"alpha": 3, "beta": 2, "gamma": 1}
    report = Statistics_Report(freq, total_words=6)

    assert report.unique_words_count() == 3
    assert report.average_word_length() == (5 * 3 + 4 * 2 + 5 * 1) / 6
    assert report.longest_word() in {"alpha", "gamma"}
    assert report.most_frequent_word() == ("alpha", 3)


def test_get_words_starting_with_is_case_insensitive_and_sorted_alphabetically():
    """Finds prefix matches regardless of prefix case and sorts results alphabetically."""
    freq = {"banana": 2, "band": 1, "bank": 4, "apple": 3}
    report = Statistics_Report(freq, total_words=10)

    assert report.get_words_starting_with("BAN") == ["banana", "band", "bank"]


def test_get_top_n_words_returns_descending_frequency_order():
    """Returns top N words sorted by count descending."""
    freq = {"alpha": 5, "beta": 2, "gamma": 4, "delta": 1}
    report = Statistics_Report(freq, total_words=12)

    assert report.get_top_n_words(3) == [("alpha", 5), ("gamma", 4), ("beta", 2)]


def test_export_report_writes_expected_format_and_values():
    """Writes report.txt-style content including headers, summary stats, and top words."""
    freq = {"python": 4, "testing": 3, "quality": 2}
    report = Statistics_Report(freq, total_words=9)
    output_name = "test_report_output.txt"
    output_path = Path("text_document_analyzer/data_output") / output_name

    try:
        report.export_report(output_name)
        output = output_path.read_text(encoding="utf-8")

        assert "----Text Analysis Report----" in output
        assert "Total Words: 9" in output
        assert "Unique Words: 3" in output
        assert "Average Word Length: 6.56" in output
        assert "Longest Word: testing" in output
        assert "Most Frequent Word: 'python' (Count: 4)" in output
        assert "Top 10 words:" in output
        assert "1. python (Count: 4)" in output
    finally:
        output_path.unlink(missing_ok=True)


def test_end_to_end_pipeline_from_input_text_to_report_file():
    """Validates complete flow: read, normalize, count, build report, and export."""
    reader = Text_Reader()
    counter = Word_Counter()

    raw_text = "The quick, brown fox jumps over the lazy dog. The fox reads docs in 2026!"
    normalized = reader.normalize_text(raw_text)
    freq = counter.count_words(normalized)
    report = Statistics_Report(freq, counter.total_words)

    output_name = "test_e2e_report.txt"
    output_path = Path("text_document_analyzer/data_output") / output_name

    try:
        report.export_report(output_name)
        output = output_path.read_text(encoding="utf-8")

        assert normalized == "the quick brown fox jumps over the lazy dog the fox reads docs in 2026"
        assert dict(freq) == {
            "quick": 1,
            "brown": 1,
            "fox": 2,
            "jumps": 1,
            "over": 1,
            "lazy": 1,
            "dog": 1,
            "reads": 1,
            "docs": 1,
            "2026": 1,
        }
        assert "Total Words: 11" in output
        assert "Unique Words: 10" in output
        assert "Most Frequent Word: 'fox' (Count: 2)" in output
    finally:
        output_path.unlink(missing_ok=True)
