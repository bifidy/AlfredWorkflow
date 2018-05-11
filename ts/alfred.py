# -*- coding: utf-8 -*-

import json

class Item(object):
    """
    Alfred display encode item model
    Reference: https://www.alfredapp.com/help/workflows/inputs/script-filter/json/
    """

    def __init__(self, title, subtitle, arg, uid=None):
        self.title = title    
        self.subtitle = subtitle
        self.uid = uid
        self.arg = arg
    
    def set_icon(self, type, path):
        self.icon = {
            "type": type,
            "path": path
        }

    @property
    def dic(self):
        return self.__dict__
    





