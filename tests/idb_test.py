#!/usr/bin/python

import pytest
import sys
import classes.iDb as db

def test_db_fetch_reviews_table():
    sql = "SELECT * FROM REVIEWS WHERE USER_ID = 12345"
    results = db.dbQuery.callDbFetch(sql)
    assert "'USER_ID': '12345'" in str(results)
    
def test_db_fetch_favorites_table():
    sql = "SELECT * FROM FAVORITES WHERE USER_ID = '12345'"
    results = db.dbQuery.callDbFetch(sql)
    assert "'USER_ID': '12345'" in str(results)

def test_db_fetch_single_result():
    sql = "SELECT * FROM REVIEWS WHERE ISBN = '5930664514'"
    results = db.dbQuery.callDbFetch(sql)
    assert results == [{'USER_ID': '54321', 'RATING': '5', 'COMMENT': 'Donec hendrerit convallis est at consequat. Aliquam pretium, nulla non aliquet interdum, tellus augue accumsan est, ac viverra leo tellus eget enim. Donec vitae auctor nisl, interdum laoreet metus. Etiam ut ligula volutpat, ornare felis ac, pharetra neque. Nunc non mi sodales, rutrum enim ut, finibus magna. Aliquam erat volutpat. Nullam orci elit, scelerisque id lectus nec, lacinia efficitur nisi.', 'ISBN': '5930664514'}]

def test_db_fetch_multiple_results():
    sql = "SELECT * FROM FAVORITES WHERE USER_ID = '12245'"
    results = db.dbQuery.callDbFetch(sql)
    assert results == [ { "USER_ID": "12245", "ISBN": "1244667890" }, { "USER_ID": "12245", "ISBN": "1244669860" }, { "USER_ID": "12245", "ISBN": "1244669890" } ]

def test_db_insert():
    sql = "INSERT INTO REVIEWS (USER_ID,RATING,COMMENT,ISBN) VALUES ('54321','5','Test','5119609250');"
    results = db.dbQuery.callDbInsert(sql)
    assert results == { "statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": "Success! 1 rows affected" }

def test_db_insert_failure():
    sql = "INSERT INTO REVIEWS (USER_ID,RATING,COMMENT,ISBN) VALUES ();"
    results = db.dbQuery.callDbInsert(sql)
    assert results != { "statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": "Success" }




