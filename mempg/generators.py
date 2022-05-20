"""
This contains the Generator class and any future sub-classes

https://github.com/initstring/mempg
MIT License
"""

import secrets
import math
import importlib.resources as pkg_resources
from . import wordlists

# To add additional formats, you simply need to edit this dict. It is set up
# to support more than one format for a given phrase length. The word type
# (i.e. 'adjective') must correlate to a text file of the same name located
# inside the package's wordlists folder. Example: adjective.txt
fmt_options = {
    2: [
        "adjective noun",
        ],
    3: [
        "adverb adjective noun",
        ],
    4: [
        "adjective noun verb-present adverb"
    ]
}


class Generator:
    """
    The Generator class is used to create passphrases of a given length.

    Optionally, you can set add_num=True to append a random 4-digit number.
    """

    def __init__(self, length, add_num=False):
        self.add_num = add_num

        # first select the format options for this length
        choices = fmt_options.get(length, None)

        # If the length is out of range, raise exception
        if not choices:
            raise ValueError("I can't count that high, sorry")

        # Randomly select one of the available format choices
        fmt = secrets.choice(choices)
        self.word_types = fmt.split(" ")

        # Calculate entropy by counting each wordlist
        list_lengths = []
        for word_type in self.word_types:
            wordlist = f"{word_type}.txt"
            words = pkg_resources.read_text(wordlists, wordlist).split("\n")
            list_lengths.append(len(words))

        combos = 1
        for length in list_lengths:
            combos = combos * length

        self.entropy = math.log2(combos)

    def make_pass(self):
        """
        Generate the passphrase using the chosen format
        """

        # Initialize empty lists for use later on
        phrase_words = []

        for word_type in self.word_types:
            # Match the word type to a corresponding wordlist file name
            wordlist = f"{word_type}.txt"

            # Process the file into a list in memory
            words = pkg_resources.read_text(wordlists, wordlist).split("\n")

            # Randomly choose one word from the list
            phrase_words.append(secrets.choice(words))

        # Here we process the chosen words in a single string - the passphrase
        phrase = " ".join(phrase_words)

        # If instructed, add a random 4-digit number to the passphrase
        # This is probably not really a great idea for actual passphrases,
        # but for the use case of creating a username it might be nice.
        if self.add_num:
            number = secrets.randbelow(10000)
            self.phrase = phrase + str(f" {number:04d}")
        else:
            self.phrase = phrase
