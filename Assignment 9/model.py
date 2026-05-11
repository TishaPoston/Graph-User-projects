class RemixModel:
    def __init__(self):
        self.current_text = ""

    # Saves the latest text
    def set_text(self, text):
        self.current_text = text

    # Makes the text uppercase
    def make_uppercase(self):
        return self.current_text.upper()

    # Makes the text lowercase
    def make_lowercase(self):
        return self.current_text.lower()

    # Reverses the text
    def reverse_text(self):
        return self.current_text[::-1]

    # Counts characters
    def count_letters(self):
        return len(self.current_text)
