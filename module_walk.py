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
        for rule in self.rules['walk']:
            raise NotImplementedError

    @property
    def module_registry(self):
        valid_modules = []
        for root, dirs, files in self.directory_root:
            valid_modules.extend(
                {fname[:-3]: os.path.join(root, fname)
                 for fname in files
                 if self.is_valid(fname, self.rules)}
            )
        return valid_modules
