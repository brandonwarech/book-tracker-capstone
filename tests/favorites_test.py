#!/usr/bin/python

import pytest
import sys
import random

import classes.favorites as f
import classes.user as u
import classes.Book as b


def test_get_favorites_by_user_int():
      favoriteObject = f.favorite()
      testUserObject = u.User('12245')
      assert f.favorite.getFavorites(favoriteObject,testUserObject) == { "statusCode": 200, "headers": { "Content-Type": "application/json" }, "body": [ { "USER_ID": "12245", "ISBN": "1244667890" }, { "USER_ID": "12245", "ISBN": "1244669860" }, { "USER_ID": "12245", "ISBN": "1244669890" } ] }
      
def test_get_favorites_by_user_string():
      favoriteObject = f.favorite()
      testUserObject = u.User('testuser2@test.com')
      assert f.favorite.getFavorites(favoriteObject,testUserObject) == { "statusCode": 200, "headers": { "Content-Type": "application/json" }, "body": [ { "USER_ID": "testuser2@test.com", "ISBN": "55555555" } ] }


def test_add_favorite():
      # self, User, Book --> switch to user_id
      random_num = random.randint(1111111,99999999999)
      book_object = b.Book(random_num,'Test','Test','Test','Test')
      favorite_object = f.favorite()
      result = f.favorite.addToFavorites(favorite_object,6666666666,book_object)
      assert result == { "statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": "Success" }


def test_remove_all_favorites():
      result = f.favorite.removeAllFromFavorites(55555)
      assert result == { "statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": "Success" }

def test_remove_book_from_favorites():
      # user_id, ISBN
      result = f.favorite.removeBookFromFavorites(55555,55555)
      assert result == { "statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": "Success" }

