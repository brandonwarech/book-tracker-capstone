#!/usr/bin/python

import pytest
import sys
import random

import classes.favorites as f
import classes.user as u
import classes.Book as b

# Create Unique Identifier for ID's for Test (primarily for "delete" tests)
random_num = random.randint(1111111,99999999999)

def test_get_favorites_by_user_int():
      user_id = 999999999
      assert f.favorite.getFavorites(user_id) == { "body": [ { "AUTHOR": "string", "CATEGORY": None, "GENRE": None, "ISBN": "get_favorites_test_isbn_int", "PUBLICATION_DATE": "string", "PUBLISHER": "string", "TITLE": "favorites INT test", "USER_ID": "999999999" } ], "headers": { "Content-Type": "application/json" }, "statusCode": 200 }
      
def test_get_favorites_by_user_string():
      user_id = "get_favorites_test_userid"
      assert f.favorite.getFavorites(user_id) == { "body": [ { "AUTHOR": "string", "CATEGORY": None, "GENRE": None, "ISBN": "get_favorites_test_isbn", "PUBLICATION_DATE": "string", "PUBLISHER": "string", "TITLE": "string", "USER_ID": "get_favorites_test_userid" } ], "headers": { "Content-Type": "application/json" }, "statusCode": 200 }

def test_add_favorite():
      book_object = b.Book(random_num,'Test','Test','Test','Test')
      favorite_object = f.favorite()
      result = f.favorite.addToFavorites(favorite_object,6666666666,book_object)
      assert result == { "statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": "Success! 1 rows affected" }

def test_add_favorite_duplicate():
      book_object = b.Book(random_num, 'Test','Test','Test','Test')
      favorite_object = f.favorite()
      result = f.favorite.addToFavorites(favorite_object,6666666666,book_object)
      assert "One or more values in the INSERT statement, UPDATE statement, or foreign key update caused by a DELETE statement are not valid because the primary key, unique constraint or unique index identified" in str(result)   

def test_add_favorite_isbn_string():
      book_object = b.Book('Test ' + str(random_num),'Test','Test','Test','Test')
      favorite_object = f.favorite()
      result = f.favorite.addToFavorites(favorite_object,6666666666,book_object)
      assert result == { "statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": "Success! 1 rows affected" }

def test_remove_book_from_favorites():

      # First add book
      book_object = b.Book(random_num,'Test','Test','Test','Test')
      favorite_object = f.favorite()
      result = f.favorite.addToFavorites(favorite_object,6666666666,book_object)

      # Then Delete It
      result = f.favorite.removeBookFromFavorites(6666666666,random_num)
      assert result == { "statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": "Success! 1 rows affected" }

def test_remove_all_favorites():

      # First add book
      book_object = b.Book(random_num,'Test','Test','Test','Test')
      favorite_object = f.favorite()
      result = f.favorite.addToFavorites(favorite_object,6666666666,book_object)

      # Then Delete It
      result = f.favorite.removeAllFromFavorites(6666666666)
      assert result == { "statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": "Success! 2 rows affected" }


def test_favorites_class_init():
      f.favorite()