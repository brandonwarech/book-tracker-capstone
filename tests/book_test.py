#!/usr/bin/python

import pytest
import sys

import classes.Book as bk

def test_book_class_init():
    book_object = bk.Book(5555555555,'Test Title','Test Author','Test Publisher','Test Publication Date')
    assert book_object.isbn == 5555555555
    assert book_object.title == 'Test Title'
    assert book_object.author == 'Test Author'
    assert book_object.publisher == 'Test Publisher'
    assert book_object.publication_date == 'Test Publication Date'

def test_book_class_init_no_value():
    with pytest.raises(Exception) as e_info:
        obj = bk.Book()
