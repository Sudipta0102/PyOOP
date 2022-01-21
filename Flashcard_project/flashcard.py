class Flashcard:
    flash = []

    def __init__(self, word : str, meaning : str):
        self.word = word
        self.meaning = meaning
        self.flash.append(self)

    def __str__(self):
        word_and_meaning = self.word + ": " + self.meaning
        # trying to append all the flashcards here
        # self.flash.append(word_and_meaning)
        return word_and_meaning

    def __repr__(self):
        return str((self.word + ":" + self.meaning))

