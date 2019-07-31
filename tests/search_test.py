#!/usr/bin/python

import pytest
import sys
import classes.search as bs

def test_book_search_isbn():
    query = bs.Search({'isbn':'9780470135006'})
    assert bs.Search.searchByQuery(query) == { "body": { "books": [ { "author": [ "Bobrow Test Preparation Services" ], "isbn": "9780470135006", "publication_date": 2008, "publisher": "Wiley Pub.", "title": "CliffsAP Chemistry (Cliffsap)" } ] }, "headers": { "Content-Type": "application/json" }, "statusCode": 200 }

def test_book_search_query():
    query = bs.Search({'query':'9780470135006'})
    assert bs.Search.searchByQuery(query) == { "body": { "books": [ { "author": [ "Bobrow Test Preparation Services" ], "isbn": "9780470135006", "publication_date": 2008, "publisher": "Wiley Pub.", "title": "CliffsAP Chemistry (Cliffsap)" } ] }, "headers": { "Content-Type": "application/json" }, "statusCode": 200 }

def test_book_search_no_params():
    query = bs.Search({'test':'test'})
    assert bs.Search.searchByQuery(query) == { "body": { "error": "Please provide search parameter" }, "headers": { "Content-Type": "application/json" }, "statusCode": 404 }
