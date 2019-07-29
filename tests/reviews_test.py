#!/usr/bin/python

import pytest
import sys
import parentpackage.classes.review as r

def test_get_reviews_by_isbn():

    query = r.Review.getReviewsByISBN('5930664514')
    assert query == [{'USER_ID': 54321, 'RATING': 5, 'COMMENT': 'Donec hendrerit convallis est at consequat. Aliquam pretium, nulla non aliquet interdum, tellus augue accumsan est, ac viverra leo tellus eget enim. Donec vitae auctor nisl, interdum laoreet metus. Etiam ut ligula volutpat, ornare felis ac, pharetra neque. Nunc non mi sodales, rutrum enim ut, finibus magna. Aliquam erat volutpat. Nullam orci elit, scelerisque id lectus nec, lacinia efficitur nisi.', 'ISBN': '5930664514'}]

def test_post_review():
    review = r.Review(54321,5119609250,5,'Test')
    post_review = r.Review.addReview(review)
    assert post_review == []
        