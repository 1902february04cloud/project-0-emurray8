#! /usr/bin/env python3
class Error(Exception):
   """Base class for exceptions"""
   pass
class InvalidWithdrawal(Error):
   """Invalid withdrawal operation. balance reduced to less than zero"""
   pass
class FileNotFound(Error):
   """Necessary data file was missing"""
   pass
class LoginFailed(Error):
    """Login failed"""
    pass