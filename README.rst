===================
myformlib
===================


USAGE
============

>>> from datetime import datetime
>>> import myformlib
>>> import attr
>>> @attr.s
... class Person:
...     name = attr.ib(type=str)
...     birthday = attr.ib(type=datetime)
>>> form = myformlib.Form(Person)
>>> form.render()
>>> p = Person(name="aodag", bithdary=datetime(1979, 8, 2))
>>> form.render(p)
