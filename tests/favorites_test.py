#!/usr/bin/python

import pytest
import sys

import parentpackage.classes.favorites as f
import parentpackage.classes.user as u


def test_get_favorites_by_user():
      favoriteObject = f.favorite()
      testUserObject = u.User(12345)
      assert f.favorite.getFavorites(favoriteObject,testUserObject) == [ { "ISBN": "1234567890", "USER_ID": "12345" }, { "ISBN": "1234667890", "USER_ID": "12345" }, { "ISBN": "1244667890", "USER_ID": "12345" } ]
      #{ "favorites": [ { "ISBN": "1234667890", "USER_ID": "12345" }, { "ISBN": "1244667890", "USER_ID": "12345" } ], "headers": { "Content-Type": "application/json" }, "statusCode": 200 }
      #[{'USER_ID': '12345', 'ISBN': '1234667890'}, {'USER_ID': '12345', 'ISBN': '1244667890'}]
      # { "favorites": [ { "ISBN": "1234667890", "USER_ID": "12345" }, { "ISBN": "1244667890", "USER_ID": "12345" } ], "headers": { "Content-Type": "application/json" }, "statusCode": 200 }


def test_get_favorites_by_user_api():
      #{ "favorites": [ { "ISBN": "1234567890", "USER_ID": "12345" }, { "ISBN": "1234667890", "USER_ID": "12345" }, { "ISBN": "1244667890", "USER_ID": "12345" } ], "headers": { "Content-Type": "application/json" }, "statusCode": 200 }
      pass

#test_get_booklist_by_booklistid()