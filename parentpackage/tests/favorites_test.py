#!/usr/bin/python

import pytest
import sys

import parentpackage.classes.favorites as f
import parentpackage.classes.user as u


def test_get_booklist_by_booklistid():
      favoriteObject = f.favorite()
      testUserObject = u.User(12345)
      assert f.favorite.getFavorites(favoriteObject,testUserObject) == {'body': {'books': [{'author': ['John Miedema'],
                              'isbn': '1936117363',
                              'publication_date': 'March 2009',
                              'publisher': 'Litwin Books',
                              'title': 'Slow reading',
                              'url': 'https://openlibrary.org/books/OL22853304M/Slow_reading'}]},
          'headers': {'Content-Type': 'application/json'},
          'statusCode': 200}

test_get_booklist_by_booklistid()