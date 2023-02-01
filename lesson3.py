# from typing import NamedTuple
#
#
# class WordSpan(NamedTuple):
#     start_pos: int
#     end_pos: int


# def get_word_spans(text):
#     words = text.split()
#     for w in words:

import typing
from typing import Dict


def count_words(text: str) -> Dict[str, int]:
    words = text.split()
    counts = dict()
    for w in words:
        if w in counts:
            counts[w] += 1
        else:
            counts[w] = 1
    return counts


class Span(typing.NamedTuple):
    """
    A representation of a substring in a shared text string.
    text[start_pos:end_pos] will return the actual substring.
    """
    text: str
    start_pos: int
    end_pos: int

    def get_substring(self):
        return self.text[self.start_pos:self.end_pos]


def get_word_spans(text):
    spans = []
    start_pos = 0
    for i, char in enumerate(text):
        if char == ' ':
            spans.append(Span(text, start_pos=start_pos, end_pos=i))
            start_pos = i + 1
    if start_pos < len(text):
        spans.append(Span(text, start_pos, len(text)))
    return spans
