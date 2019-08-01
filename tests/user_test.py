#!/usr/bin/python

import pytest
import sys

import classes.user as U

def test_user_class_init():
    user_object = U.User('testuser1@test.com')
    assert user_object.user_id == 'testuser1@test.com'

def test_user_class_init_no_value():
    with pytest.raises(Exception) as e_info:
        obj = U.User()
