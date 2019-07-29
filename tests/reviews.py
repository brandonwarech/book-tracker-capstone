#!/usr/bin/python

import pytest
import sys
import parentpackage.classes.review as r

def test_book_search_isbn():
    
    query = r.Search({'isbn':'9780470135006'})
    assert bs.Search.searchByQuery(query) == { "body": { "books": [{ "author": ["Bobrow Test Preparation Services"], "isbn": "9780470135006", "publication_date": 2008, "publisher": "Cliffs Notes", "title": "CliffsAP Chemistry (Cliffsap)" }] }, "headers": { "Content-Type": "application/json" }, "statusCode": 200 }


        