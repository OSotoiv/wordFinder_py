from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary.
    >>> words = WordFinder('./special_list.txt')
    9 words found

    >>> words.random() in ['kale','parsnips', 'apple', 'mango', '# Veggies', '# Fruits', '']
    True
    >>> words.random() in ['kale','parsnips', 'apple', 'mango', '# Veggies', '# Fruits', '']
    True
    >>> words.random() in ['kale','parsnips', 'apple', 'mango', '# Veggies', '# Fruits', '']
    True
    >>> words.random() in ['kale','parsnips', 'apple', 'mango', '# Veggies', '# Fruits', '']
    True
    """

    def __init__(self, file, parent=True):
        self.file_url = file
        if parent:
            self.words = self.get_list(file)

    def __repr_(self):
        """returns rep of function"""
        return f"<WordFinder(file={self.file_url})"

    def get_list(self, file):
        with open(file) as f:
            data = f.read()
        data = data.strip()
        all_words = [word for word in data.split('\n')]
        print(f"{len(all_words)} words found")
        return all_words

    def random(self):
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """Finds random words from dictionary filtering out comments and spaces
    >>> words = SpecialWordFinder('./special_list.txt')
    4 words found

    >>> words.random() in ['kale','parsnips', 'apple', 'mango']
    True
    >>> words.random() in ['kale','parsnips', 'apple', 'mango']
    True
    >>> words.random() in ['kale','parsnips', 'apple', 'mango']
    True
    >>> words.random() in ['kale','parsnips', 'apple', 'mango']
    True

    """

    def __init__(self, file):
        """Creates subclass of WordFinder with filtered word list"""
        super().__init__(file, False)
        self.words = self.get_and_filter_list(file)

    def get_and_filter_list(self, file):
        """reads file and filters for empty lines and #comments"""
        with open(file) as f:
            data = f.read()
        data = data.strip()

        def is_word(word):
            return word != '' and not word.startswith("#")
        all_words = [word for word in data.split('\n') if is_word(word)]
        print(f"{len(all_words)} words found")
        return all_words
