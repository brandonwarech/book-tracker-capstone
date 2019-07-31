#!/usr/bin/python

import pytest
import sys
import classes.review as r

def test_get_reviews_by_isbn():
    query = r.Review.getReviewsByISBN('5930664514')
    assert query == { "body": { "reviews": [ { "COMMENT": "Donec hendrerit convallis est at consequat. Aliquam pretium, nulla non aliquet interdum, tellus augue accumsan est, ac viverra leo tellus eget enim. Donec vitae auctor nisl, interdum laoreet metus. Etiam ut ligula volutpat, ornare felis ac, pharetra neque. Nunc non mi sodales, rutrum enim ut, finibus magna. Aliquam erat volutpat. Nullam orci elit, scelerisque id lectus nec, lacinia efficitur nisi.", "ISBN": "5930664514", "RATING": "5", "USER_ID": "54321" } ] }, "headers": { "Content-Type": "application/json" }, "statusCode": 200 }

def test_post_review():
    review = r.Review(54321,5119609250,5,'Test')
    post_review = r.Review.addReview(review)
    assert post_review == {'body': 'Success', 'headers': {'Content-Type': 'application/json'}, 'statusCode': 200}

def test_get_reviews_by_user():
    assert False

def test_delete_review():
    result = r.Review.deleteReview(54321,5119609250)
    assert result == { "statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": "Success" }