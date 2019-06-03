#!/usr/bin/python

import pytest
import sys
import book_search as bs

def test_book_search_isbn():
    assert bs.search({'isbn':'9780980200447'}) == {'body': {'books': [{'author': ['John Miedema'],
                              'isbn': '1936117363',
                              'publication_date': 'March 2009',
                              'publisher': 'Litwin Books',
                              'title': 'Slow reading',
                              'url': 'https://openlibrary.org/books/OL22853304M/Slow_reading'}]},
          'headers': {'Content-Type': 'application/json'},
          'statusCode': 200}

def test_book_search_author():
    assert bs.search({'author':'Rusty Williams'}) == {
  "body": {
    "books": [{
      "author": ["Rusty Williams"],
      "isbn": "159330126X",
      "publication_date": "November 30, 2003",
      "publisher": "Aventine Press",
      "title": "Scatterlings",
      "url": "https://openlibrary.org/books/OL12381389M/Scatterlings"
    }]
  },
  "headers": {
    "Content-Type": "application/json"
  },
  "statusCode": 200
}

          
def test_book_search_no_params():
    assert bs.search({'test':'test'}) == {
        "body": {
            "error": "Please provide search parameter"
        },
        "headers": {
            "Content-Type": "application/json"
        },
        "statusCode": 404
        }

def test_book_search_title():
    assert bs.search({'title':'Child Called It'}) == {
    "body": {
        "books": [{
        "author": ["David J. Pelzer"],
        "isbn": "0929099028",
        "publication_date": "1993",
        "publisher": "Omaha Press Publishing Company, Inc",
        "title": "A child called it",
        "url": "https://openlibrary.org/books/OL845571M/A_child_called_it"
        }, {
        "author": ["David J. Pelzer"],
        "isbn": "075284170X",
        "publication_date": "January 23, 2001",
        "publisher": "Orion (an Imprint of The Orion Publishing Group Ltd )",
        "title": "A Child Called It",
        "url": "https://openlibrary.org/books/OL7984181M/A_Child_Called_It"
        }, {
        "author": ["David J. Pelzer"],
        "isbn": "0739400614",
        "publication_date": "1995",
        "publisher": "Health Communications",
        "title": "A Child called \"it\" and The lost boy",
        "url": "https://openlibrary.org/books/OL20941782M/A_Child_called_it_and_The_lost_boy"
        }, {
        "author": ["David J. Pelzer"],
        "isbn": "9796864002",
        "publication_date": "2003",
        "publisher": "Gramedia Pustaka Utama",
        "title": "A child called 'It'",
        "url": "https://openlibrary.org/books/OL25569251M/A_child_called_'It'"
        }, {
        "author": ["David J. Pelzer"],
        "isbn": "0739400614",
        "publication_date": "1995",
        "publisher": "Health Communications",
        "title": "A Child called \"it\" and The lost boy",
        "url": "https://openlibrary.org/books/OL20941782M/A_Child_called_it_and_The_lost_boy"
        }, {
        "author": ["Dave Pelzer"],
        "isbn": "0795345577",
        "publication_date": "Apr 07, 2015",
        "publisher": "RosettaBooks",
        "title": "Too Close to Me: The Middle-Aged Consequences of Revealing a Child Called It",
        "url": "https://openlibrary.org/books/OL26810439M/Too_Close_to_Me_The_Middle-Aged_Consequences_of_Revealing_a_Child_Called_It"
        }]
    },
    "headers": {
        "Content-Type": "application/json"
    },
    "statusCode": 200
    }