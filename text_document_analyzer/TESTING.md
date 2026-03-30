# TESTING.md

## Text Document Analyzer: Testing Instructions

This document explains how to run and maintain automated tests for the `text_document_analyzer` module using `pytest`.

## Scope

These tests cover only the Text Document Analyzer assignment and do not include payroll tests.

## Test Location

Primary test file:

- `text_document_analyzer/tests/test_text_analyzer.py`

## Prerequisites

- Python 3.8+
- Virtual environment created at project root (`.venv`)
- `pytest` installed in the active environment

## Environment Setup

From the repository root, activate the virtual environment:

```bash
source .venv/bin/activate
```

Install `pytest` if needed:

```bash
python3 -m pip install pytest
```

## Running Tests

Run only the analyzer tests:

```bash
python3 -m pytest text_document_analyzer/tests/test_text_analyzer.py
```

Run with verbose output:

```bash
python3 -m pytest -v text_document_analyzer/tests/test_text_analyzer.py
```

Run all project tests (optional):

```bash
python3 -m pytest
```

## What Is Covered

The analyzer test suite validates:

- File reading behavior for existing and missing input files
- Text normalization (lowercase conversion, punctuation removal, whitespace cleanup)
- Word counting rules:
  - ignore stop words
  - ignore words shorter than 3 characters
  - count valid words and totals accurately
- Statistics generation:
  - total words
  - unique words
  - average word length
  - longest word
  - most frequent word
- Utility methods:
  - top N words sorted by frequency descending
  - words starting with a prefix sorted alphabetically
- Report export format and expected content
- End-to-end flow from raw input text to generated report output

## Notes on Test Data

- Sample text input for manual runs is in:
  - `text_document_analyzer/data_input/input.txt`
- Report output is written to:
  - `text_document_analyzer/data_output/report.txt`
- Some tests create temporary fixture/report files and remove them afterward.

## Troubleshooting

If you see command not found errors:

1. Ensure the virtual environment is activated.
2. Use `python3 -m pytest` instead of `pytest` directly.

If imports fail:

- Run tests from the repository root directory.
- Confirm package/module paths were not renamed.

## Test Writing Rules

When adding new tests to this module:

- Keep tests focused on Text Document Analyzer functionality only.
- Include documentation for each test (docstring or clear comment).
- Use descriptive test names that explain the expected behavior.
