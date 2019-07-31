#!/usr/bin/python

import pytest
import sys

import classes.Friend as f
import classes.user as u



def test_get_friends_by_user():
      assert f.Friend.getFriends(12345) == None
      #{ "favorites": [ { "ISBN": "1234667890", "USER_ID": "12345" }, { "ISBN": "1244667890", "USER_ID": "12345" } ], "headers": { "Content-Type": "application/json" }, "statusCode": 200 }
      #[{'USER_ID': '12345', 'ISBN': '1234667890'}, {'USER_ID': '12345', 'ISBN': '1244667890'}]
      # { "favorites": [ { "ISBN": "1234667890", "USER_ID": "12345" }, { "ISBN": "1244667890", "USER_ID": "12345" } ], "headers": { "Content-Type": "application/json" }, "statusCode": 200 }
