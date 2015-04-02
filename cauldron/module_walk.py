import os


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
        for rule in self.rules['walk']:
            if not rule(fname):
                return False
        return True

    def construct_module_name(self, root, fname):
        """
        TODO
        """
        fname = fname.rsplit('.', 1)[0]
        root = root.replace(self.directory_root + os.sep, '')
        return '.'.join(os.path.join(root, fname).split(os.sep))

    @property
    def module_registry(self):
        valid_modules = {}
        for root, dirs, files in os.walk(self.directory_root):
            valid_modules.update(
                {self.construct_module_name(root, fname):
                 os.path.join(root, fname)
                 for fname in files
                 if self.is_valid(root, fname)}
            )
        return valid_modules
