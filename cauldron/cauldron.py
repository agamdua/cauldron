# -*- coding: utf-8 -*-
from config import RULES

from object_cache import ObjectCache


# oc = ObjectCache(rules=RULES)


def debug(obj_cache):
    from pprint import pprint
    pprint(obj_cache.modules)
    print("Number of files/modules = {}".format(len(obj_cache.modules)))
    pprint(obj_cache.members)
    print(
        "Number of classes satisfying criteria = {}"
        .format(len(obj_cache.members))
    )
