import re

class Text_Reader:
    def read_file(self, file_path):
        try:
            with open(f"text_document_analyzer/data_input/{file_path}", 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
            return None
        except IOError as e:
            print(f"Error reading file '{file_path}': {e}")
            return None

    def normalize_text(self, text: str) -> str:
        if text is None:
            return ""
        text = text.lower()

        # Removing punctuation and special characters
        text = re.sub(r"[^a-z0-9\s]", "", text)

        # Removing extra whitespace
        text = re.sub(r"\s+", " ", text).strip()

        return text