#!/usr/bin/python3
"""Defines an abject attribute lookup function"""


def lookup(obj):
    """ returns a list of possible attributes """
    return (dir(obj))
