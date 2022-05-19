# Memorable Passphrase Generator (MemPG)

## Overview

This is a proof-of-concept to generate passphrases that are hard to guess but easy to remember. Other passphrase generators simply produce random words, with no thought to how they flow together.

The idea here is to define some structures that resemble sentences, and then to leverage large word-lists specific to parts-of-speech (adjectives, nouns, verbs, etc) to fill them in randomly.

This is done by defining a passphrase format for various lengths. For example:

`"adjective noun verb-present adverb"`

Then, we randomly select the correct word type from word-lists organized by parts of speech. We end up with a phrase that can hopefully evoke a mini-story in our heads, without choosing something guessable like a song lyric or a movie quote.

Here are some real examples generated with this tool:

````
uncensored patriarch shops grotesquely
````

**TO DO**:
- [X] Basic working PoC
- [ ] Build phrase format up to 8 words
- [ ] Review / improve wordlists
- [ ] Publish on PyPI (maybe)



## Usage

When running the tool from the cloned source, leverage the helper script in the root directory. Example:

```
mempg.sh -l4 -p 10
```

The tool accepts two optional parameters:

```
  -l LENGTH, --length LENGTH    Length of passphrase to generate. Default: 6
  -n, --numbers                 Add random digits to end of phrase Default: False
  -p PHRASES, --phrases PHRASES How many phrases to generate. Default: 1
```

Each run will generate 1 passphrase, and the entropy for that phrase will be displayed. This entropy number is a simple calculation based on the length of the input wordlists for each word.

## Sources

I've sourced the word-lists from the following locations:

- [WordNet](https://wordnet.princeton.edu/) from Princeton University:
    - nouns
    - adverbs
    - adjectives
    - verbs

## Warnings

Please don't bet your life or your money on my crappy Python script. I'm just some guy on the Internet, hobbling code together and crossing my fingers.

Obviously, the shorter the phrase, the less safe it is. The tool will allow you to create 2-word phrases. I figured these might be handy for random usernames or something.

There are surely flaws with this approach. Please open issues to tell me what a fool I am for doing this or that, so I can hopefully improve it. Thanks!
