#!/usr/bin/python

import pytest
import sys
import classes.iDb as db


def test_db_fetch_reviews_table():
    #sql = "SELECT * FROM REVIEWS WHERE ISBN = 3622859490"
    #sql = "SELECT * FROM FAVORITES WHERE USER_ID = 12345"
    sql = "SELECT * FROM REVIEWS WHERE USER_ID = 12345"
    query_object = db.dbQuery(sql)
    results = db.dbQuery.callDbFetch(query_object)
    assert "'USER_ID': '12345'" in str(results)
    
def test_db_fetch_favorites_table():
    #sql = "SELECT * FROM REVIEWS WHERE ISBN = '5930664514'"
    sql = "SELECT * FROM FAVORITES WHERE USER_ID = 12345"
    query_object = db.dbQuery(sql)
    results = db.dbQuery.callDbFetch(query_object)
    assert results == [{'USER_ID': '12345', 'ISBN': '1234567890'}, {'USER_ID': '12345', 'ISBN': '1234667890'}, {'USER_ID': '12345', 'ISBN': '1244667890'}]

def test_db_fetch_single_result():
    sql = "SELECT * FROM REVIEWS WHERE ISBN = '5930664514'"
    query_object = db.dbQuery(sql)
    results = db.dbQuery.callDbFetch(query_object)
    assert results == [{'USER_ID': '54321', 'RATING': '5', 'COMMENT': 'Donec hendrerit convallis est at consequat. Aliquam pretium, nulla non aliquet interdum, tellus augue accumsan est, ac viverra leo tellus eget enim. Donec vitae auctor nisl, interdum laoreet metus. Etiam ut ligula volutpat, ornare felis ac, pharetra neque. Nunc non mi sodales, rutrum enim ut, finibus magna. Aliquam erat volutpat. Nullam orci elit, scelerisque id lectus nec, lacinia efficitur nisi.', 'ISBN': '5930664514'}]

def test_db_fetch_multiple_results():
    sql = "SELECT * FROM FAVORITES WHERE USER_ID = 12345"
    query_object = db.dbQuery(sql)
    results = db.dbQuery.callDbFetch(query_object)
    assert results == [{'USER_ID': '12345', 'ISBN': '1234567890'}, {'USER_ID': '12345', 'ISBN': '1234667890'}, {'USER_ID': '12345', 'ISBN': '1244667890'}]


def test_db_insert():
    sql = "INSERT INTO REVIEWS (USER_ID,RATING,COMMENT,ISBN) VALUES ('54321','5','Test','5119609250');"
    query_object = db.dbQuery(sql)
    results = db.dbQuery.callDbInsert(query_object)
    assert results == { "statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": "Success" }




