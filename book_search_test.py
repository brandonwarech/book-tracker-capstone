#!/usr/bin/python

import pytest
import sys
import book_search as bs

def test_book_search():
    assert bs.search({'test':'test'}) != None