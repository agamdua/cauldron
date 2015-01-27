import os


class ModuleWalk(object):
    """
    Enables us to walk through the other modules
    """
    def __init__(self, directory_root=None):
        """
        Sets the variables required for walking
        """
        if not directory_root:
            self.directory_root = os.getcwd()
        else:
            self.directory_root = directory_root

    @classmethod
    def walk(self):
        raise NotImplementedError
