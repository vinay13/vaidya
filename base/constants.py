# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# Standard Library
import inspect



def _user_attributes(cls):
    defaults = dir(type(str('defaults'), (object,), {}))  # gives all inbuilt attrs
    return [
        item[0] for item in inspect.getmembers(cls) if item[0] not in defaults]



def choices(cls):
    """
    Decorator to set `CHOICES` and other attributes
    """
    _choices = []
    for attr in _user_attributes(cls):
        val = getattr(cls, attr)
        setattr(cls, attr[1:], val[0])
        _choices.append((val[0], val[1]))
    setattr(cls, 'CHOICES', tuple(_choices))
    return cls



@choices
class ComplaintStatus:
    _OPEN = [1, "Open"]
    _CLOSED = [2, "Closed"]
    _ASSIGNED = [3, "Assigned"]
    _REOPEN = [4 , "Reopen"]



@choices 
class PollOptions :
    _SINGLE = [1,"SINGLE"]
    _MULTIPLE = [2, "MULTIPLE"]


@choices
class PollType:
    _SCHOOL = [1,"SCHOOL"] 
    _CLASS =  [2,"CLASS"]



@choices
class EventType:
    _HOUSE =    [1,"HOUSE"]
    _CLASS =    [2,"CLASS"]
    _SCHOOL =   [3,"SCHOOL"]
    _NATIONAL = [4,"NATIONAL"]
    _RESTRICTED = [5,"RESTRICTED"]
    _EXAM =[6,"EXAM"]



