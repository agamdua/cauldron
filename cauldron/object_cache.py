import inspect
import os
import imp

from cached_property import cached_property as cached

from config import RULES
from module_walk import ModuleWalk


class NoValidationError:
    pass


class ObjectCache(object):
    """
    Store for all the objects that satisfy rules
    """
    def __init__(self, rules=None, disable_validation=False, inspection=True):
        """
        Instantiate the object cache with whatever validation rules
        are required

        These will ideally be sourced from a `settings` file.

        :param rules: all validation rules for storage
        :default rules: None
        :param disable_validation: no rules will be expected
        :default disable_validation: False
        """
        self.rules = rules
        self.disable_validation = disable_validation
        self.inspection = inspection

    @cached
    def modules(self, directory_root=os.getcwd()):
        """
        walking the modules, looking for what we need

        Attributes:
            directory_root -- defaults to current directory, used in os.walk()
        """
        if self.rules and not self.disable_validation:
            return ModuleWalk(
                rules=self.rules,
                directory_root=directory_root,
                inspection=self.inspection
            ).module_registry
        else:
            raise NoValidationError(
                "Please define rules or explicitly use"
                "the disable_validation flag"
            )

    @cached
    def members(self):
        _members = []
        for module in self.modules.keys():
            for obj in inspect.getmembers(
                imp.load_source(module, self.modules[module])
            ):
                if all([rule(obj) for rule in self.rules['inspect']]):
                    _members.append(obj[1])
        return list(set(_members))


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
