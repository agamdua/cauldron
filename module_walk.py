import os
import itertools

from inspection import Inspect


class ModuleWalk(object):
    """
    Enables us to walk through the other modules
    """
    def __init__(self, rules=None, directory_root=None, inspection=True):
        """
        Sets the variables required for walking
        """
        self.rules = rules
        self.directory_root = directory_root
        self.inspection = inspection

    def is_valid(self, root, fname):
        """
        This methods runs over the rules specified to the object cache and
        validates the module according to them.
        """
        # TODO: exit when first condition fails, no need to evaluate all and
        # do and all() on top of that.
        if all([rule(fname) for rule in self.rules['walk']]):
            if self.inspection:
                module = Inspect.import_module(root, fname)
                return all([rule(module) for rule in self.rules['inspect']])
            else:
                return True
        return False

    @property
    def module_registry(self):
        valid_modules = {}
        for root, dirs, files in os.walk(self.directory_root):
            _dirs = filter(lambda x: not x.startswith('.'), dirs)
            if _dirs:
                continue
            else:
                # TODO: this will overwrite the value in the dict if it exists.
                # This is not the expected behavior and needs to change.
                valid_modules.update(
                    {fname[:-3]: os.path.join(root, fname)
                     for fname in files
                     if self.is_valid(root, fname)}
                )
        return valid_modules
