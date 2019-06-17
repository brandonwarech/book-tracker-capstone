#!/usr/bin/python

import pytest
import sys
import book_list as bl

def test_get_booklist_by_booklistid():
    assert bl.getBookList({'user_id':'12345'}) == {'body': {'books': [{'author': ['John Miedema'],
                              'isbn': '1936117363',
                              'publication_date': 'March 2009',
                              'publisher': 'Litwin Books',
                              'title': 'Slow reading',
                              'url': 'https://openlibrary.org/books/OL22853304M/Slow_reading'}]},
          'headers': {'Content-Type': 'application/json'},
          'statusCode': 200}
