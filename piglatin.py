
class PigLatin:
    def __init__(self):
        self.phrase = ""

    def get_phrase(self, phrase=None, expected=None):
        if phrase is not None and expected is not None:
            self.phrase = phrase
        return self.phrase

