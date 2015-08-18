import imp


class Inspect(object):
    """
    Inspects the modules that have been collected and filters
    based on rules provided.
    """
    @classmethod
    def get_members_based_on(self, root, fname):
        return imp.load_source(fname, root)
