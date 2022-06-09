"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("words.txt")
    3 words in file

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.randomWord() in ["cat", "dog", "porcupine"]
    True
    """
    def __init__(self, path):
        text_file= open(path)

        self.words = self.parse(text_file)

        print(f"{len(self.words)} words in file")

    def parse(self, text_file):

        return [words.strip for words in text_file]

    def randomWord(self):
        
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words in file

    >>> swf.randomWord() in ["pear", "carrot", "kale"]
    True

    >>> swf.randomWord() in ["pear", "carrot", "kale"]
    True

    >>> swf.randomWord() in ["pear", "carrot", "kale"]
    True
    """

    def parse(self, text_file):
        """Parse text_file -> list of words, skipping blanks/comments."""

        return [words.strip() for words in text_file
                if words.strip() and not words.startswith("#")]        

