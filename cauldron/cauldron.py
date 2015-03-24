# -*- coding: utf-8 -*-
from config import RULES

from object_cache import ObjectCache


object_cache = ObjectCache(rules=RULES)


def debug(object_cache):
    from pprint import pprint
    pprint(object_cache.modules)
    print("Number of files/modules = {}".format(len(object_cache.modules)))
    pprint(object_cache.members)
    print(
        "Number of classes satisfying criteria = {}"
        .format(len(object_cache.members))
    )

debug(object_cache)
