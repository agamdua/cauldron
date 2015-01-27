import itertools
import os


class ModuleWalk(object):
    """
    Enables us to walk through the other modules
    """
    def __init__(self, rules=None, directory_root=None):
        """
        Sets the variables required for walking
        """
        self.rules = rules
        self.directory_root = directory_root

    def is_valid(self, fname):
        if all([
            rule(fname) for rule in self.rules['walk']
        ]):
            return fname

    @property
    def module_registry(self):
        valid_modules = {}
        for root, dirs, files in os.walk(self.directory_root):
            _dirs = list(
                itertools.ifilter(lambda x: not x.startswith('.'), dirs)
            )
            if _dirs:
                # need an ignore setting
                continue
            else:
                valid_modules.update(
                    {fname[:-3]: os.path.join(root, fname)
                     for fname in files
                     if self.is_valid(fname)}
                )
        return valid_modules
