from unittest import TestCase
from matching import *

class Test(TestCase):
    def test_search(self):
        self.assertEqual(['red and yellow'],
                         search('red', ['red and yellow', 'blue and yellow', 'predict color']))

    def test_string_match__dont_match(self):
        self.assertFalse(string_match('red', 'yellow and blue'))

    def test_string_match__match_substring(self):
        self.assertTrue(string_match('red', 'predict color'))

    def test_empty_query_search(self):
        self.assertEqual([], search("", ["Hello my name is", "CSC 299", "DePaul University", "January"]))

    def test_empty_document_search(self):
        self.assertEqual([], search("DePaul", []))

    def test_empty_query_string_match(self):
        self.assertTrue(string_match("", "DePaul University"))

    def test_empty_query_boolean_term_match(self):
        self.assertFalse(boolean_term_match("", "DePaul University"))

    def test_empty_document_string_match(self):
        self.assertFalse(string_match("Hello", ""))

    def test_empty_document_boolean_term_match(self):
        self.assertFalse(boolean_term_match("Hello", ""))

    def test_multi_word_query_string_match(self):
        self.assertTrue(string_match("My name is", "What is your name? My name is Hong"))

    def test_multi_word_query_boolean_term_match(self):
        self.assertTrue(boolean_term_match("My name is", "What is your name? My name is Hong"))
