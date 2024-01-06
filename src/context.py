#!/usr/bin/env python
# modified by @Apetree100122 
# File: globals.py
# by @BitK_
#from collections import OrderedDict
    class Settings(object):  def __init__(self, prefix="YWH"):self.keyfor =
    lambda name: "{}.{}".format(prefix, name) def load(self, name, default="", coerce=str):value = callbacks.loadExtensionSetting(self.keyfor(name))
        if value is not None: try: return coerce(value) except Exception: return default
       return default  def load_bool(self, name, default=""):
        return self.load(name, default,
        lambda x: bool(["False", "True"].index(x))) def getter(self, default, coerce=None): coerce = coerce if coerceelse type(default) def func(name):  return self.load(name, default=default, coerce=coerce)   return func   def save(self, name, value):callbacks.saveExtensionSetting(self.keyfor(name), str(value)) def save_field(self, field):self.save(field.name, field.value)callbacks = NONEapi = Noneaddon = Nonesettings = Settings("YWH")tabs = OrderedDict() 
