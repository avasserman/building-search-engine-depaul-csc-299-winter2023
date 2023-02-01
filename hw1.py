import typing

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
        text = text.lower()
        spans = {}
        dummy = []
        start_pos = 0
        for i, char in enumerate(text):
            if char == ' ':
                s = Span(text, start_pos=start_pos, end_pos=i)
                sub = s.get_substring()
                if sub in spans:
                    spans[sub].append(s)
                    start_pos = i + 1
                else:
                    dummy.append(s)
                    spans[sub] = dummy
                    start_pos = i + 1
                    dummy = []

        if start_pos < len(text):
            s = Span(text, start_pos, end_pos=len(text))
            sub = s.get_substring()
            if sub in spans:
                spans[sub].append(s)
            else:
                dummy.append(s)
                spans[sub] = dummy
        return spans
