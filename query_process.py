from typing import List

import tokenizer
from documents import DocumentCollection, Document
from index import Index
from tokenizer import Tokenizer, NaiveTokenizer


class QueryTransformer:
    def process_query(self, query: str) -> List[str]:
        pass


class TokenizerOnlyQueryTransformer(QueryTransformer):
    def __init__(self, tokenizer: Tokenizer):
        self.tokenizer = tokenizer

    def process_query(self, query: str) -> List[str]:
        return self.tokenizer.tokenize(query)


class ResultFormatter:
    def format_results(self, results: List[str]) -> str:
        """
        Given a list of doc_ids corresponding to the results of search create a string describing
        these results to be presented to the user.
        :param results: List of doc_ids
        :return: A single string presented to the user.
        """
        raise NotImplemented


class NaiveResultFormatter(ResultFormatter):
    def __init__(self, document_collection: DocumentCollection):
        self.document_collection = document_collection

    @staticmethod
    def format_single_result(doc: Document) -> str:
        return doc.text

    def format_results(self, results: List[str]) -> str:
        out = ''
        for doc_id in results:
            doc = self.document_collection.get(doc_id)
            out += '\n' + self.format_single_result(doc)
        return out


class QueryProcess:
    def __init__(self, index: Index,
                 query_transformer: QueryTransformer, result_formatter: ResultFormatter):
        self.index = index
        self.query_transformer = query_transformer
        self.result_formatter = result_formatter

    @staticmethod
    def create_naive_query_process(documents: DocumentCollection, index: Index) -> 'QueryProcess':
        return QueryProcess(
            index=index,
            query_transformer=TokenizerOnlyQueryTransformer(tokenizer=tokenizer.NaiveTokenizer()),
            result_formatter=NaiveResultFormatter(documents)
        )

    def run(self, query: str) -> str:
        processed_query = self.query_transformer.process_query(query)
        results = self.index.search(processed_query)
        formatted_results = self.result_formatter.format_results(results)
        return formatted_results

