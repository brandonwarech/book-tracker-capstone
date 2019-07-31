#!/usr/bin/python

import pytest
import sys

import classes.favorites as f
import classes.user as u


def test_get_favorites_by_user():
      favoriteObject = f.favorite()
      testUserObject = u.User(12345)
      assert f.favorite.getFavorites(favoriteObject,testUserObject) == [ { "ISBN": "1234567890", "USER_ID": "12345" }, { "ISBN": "1234667890", "USER_ID": "12345" }, { "ISBN": "1244667890", "USER_ID": "12345" } ]
      #{ "favorites": [ { "ISBN": "1234667890", "USER_ID": "12345" }, { "ISBN": "1244667890", "USER_ID": "12345" } ], "headers": { "Content-Type": "application/json" }, "statusCode": 200 }
      #[{'USER_ID': '12345', 'ISBN': '1234667890'}, {'USER_ID': '12345', 'ISBN': '1244667890'}]
      # { "favorites": [ { "ISBN": "1234667890", "USER_ID": "12345" }, { "ISBN": "1244667890", "USER_ID": "12345" } ], "headers": { "Content-Type": "application/json" }, "statusCode": 200 }

def test_add_favorite():
      # self, User, Book --> switch to user_id
      assert False

def test_remove_all_favorites():
      result = f.favorite.removeAllFromFavorites(55555)
      assert result == { "statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": "Success" }

def test_remove_book_from_favorites():
      # user_id, ISBN
      result = f.favorite.removeBookFromFavorites(55555,55555)
      assert result == { "statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": "Success" }

