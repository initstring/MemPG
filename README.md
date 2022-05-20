# Memorable Passphrase Generator (MemPG)

## Overview

This is a proof-of-concept to generate passphrases that are hard to guess but easy to remember. Other passphrase generators simply produce random words, with no thought to how they flow together.

The idea here is to define some structures that resemble sentences, and then to leverage large word-lists specific to parts-of-speech (adjectives, nouns, verbs, etc) to fill them in randomly.

This is done by defining a passphrase format for various lengths. For example:

`"adjective noun verb-present adverb"`

Then, we randomly select the correct word type from word-lists organized by parts of speech. We end up with a phrase that can hopefully evoke a mini-story in our heads, without choosing something guessable like a song lyric or a movie quote.

Here are some real examples generated with this tool:

````
# 28 bits of entropy:
stormbound jitters

# 40 bits of entropy:
neglectfully unpasteurized indoctrination

# 52 bits of entropy:
uncensored patriarch shops grotesquely

# 61 bits of entropy:
tricycle trawls covertly outside saipan

# 87 bits of entropy:
powered monarchist digitizes permissibly beneath revalueing offer

(... more to come, still a work in progress)
````

## Usage

When running the tool from the cloned source, leverage the helper script in the root directory. Example:

```
mempg.sh -l4 -p 10
```

The tool accepts three optional parameters:

```
  -l LENGTH, --length LENGTH    Length of passphrase to generate. Default: 6
  -n, --numbers                 Add random digits to end of phrase Default: False
  -p PHRASES, --phrases PHRASES How many phrases to generate. Default: 1
```

Each run will generate a simply entropy calculation, based on the length of the input wordlists for each word selected.

## Contributing

Please open an issue to start a discussion on any major contributions. For any small fixes, just submit a PR. Thank you!

Right now, I am particularly interested in help with making the phrases sound more natural. This might include improving/curating some of the wordlists, as well as modifying or adding additional phrase formats as defined in `fmt_options` inside `generators.py`.

## Sources

I've sourced the word-lists from the following locations:

- [WordNet](https://wordnet.princeton.edu/) from Princeton University:
    - nouns
    - adverbs
    - adjectives
    - verbs
- Wikipedia:
    - [prepositions](https://en.wikipedia.org/wiki/List_of_English_prepositions) (prototypical, conjunctive)

## Warnings

Please don't bet your life or your money on my crappy Python script without fully understanding what it is doing. I'm just some guy on the Internet, hobbling code together and crossing my fingers.

Human memory isn't the best device to manage lots of passwords. However, we do need to remember SOME passwords - like the one to unlock your password manager, for instance. Understand what you are protecting and what type of password attack you are defending against (online, offline, etc) fully before using a tool like this.

There are surely flaws with this approach. Please open issues to tell me what a fool I am for doing this or that, so I can hopefully improve it. Thanks!
