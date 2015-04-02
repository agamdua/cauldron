# -*- coding: utf-8 -*-
import importlib
import os

from cached_property import cached_property as cached

from module_walk import ModuleWalk


class NoValidationError:
    pass


class ObjectCache(object):
    """
    Store for all the objects that satisfy rules
    """
    def __init__(self,
                 rules=None,
                 disable_validation=False,
                 inspection=True,
                 root=os.getcwd()):
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
        self.root = root

    @cached
    def modules(self):
        """
        walking the modules, looking for what we need

        Attributes:
            directory_root -- defaults to current directory, used in os.walk()
        """
        if self.rules and not self.disable_validation:
            return ModuleWalk(
                rules=self.rules,
                directory_root=self.root,
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
            try:
                objects = vars(importlib.import_module(module)).items()
            except Exception:
                # TODO: log this
                continue
            for obj in objects:
                if self.is_valid(obj):
                    _members.append(obj[1])
        return list(set(_members))

    def is_valid(self, obj):
        """
        TODO
        """
        for rule in self.rules['inspect']:
            if not rule(obj):
                return False
        return True
