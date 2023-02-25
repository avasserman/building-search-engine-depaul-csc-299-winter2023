from unittest import TestCase

import documents
from index import InvertedTfIdfIndex, TfIdfIndex


class TestTfIdfIndex(TestCase):
    def test_search(self):
        idx = TfIdfIndex()
        idx.add_document(documents.TransformedDocument(doc_id='1', tokens=['a', 'b', 'c', 'a']))
        idx.add_document(documents.TransformedDocument(doc_id='2', tokens=['a', 'b']))
        idx.add_document(documents.TransformedDocument(doc_id='3', tokens=['a', 'b', 'c', 'c']))
        # 'c' is in fewer documents, so the weight is higher.
        self.assertEqual(['3', '1'], idx.search(['a', 'c']))


class TestInvertedTfIdfIndex(TestCase):
    # The results should be exactly the same. Inverted index is just faster.
    def test_search(self):
        idx = InvertedTfIdfIndex()
        idx.add_document(documents.TransformedDocument(doc_id='1', tokens=['a', 'b', 'c', 'a']))
        idx.add_document(documents.TransformedDocument(doc_id='2', tokens=['a', 'b']))
        idx.add_document(documents.TransformedDocument(doc_id='3', tokens=['a', 'b', 'c', 'c']))
        # 'c' is in fewer documents, so the weight is higher.
        self.assertEqual(['3', '1'], idx.search(['a', 'c']))
