"""
Utils that assume what you are doing

(Here be dragons)
"""

def silence(func, x, exceptions=None, fail=False):
    """
    This is a wrapper that silences exceptions in a callable.

    At the moment it assumes there is only one variable required
    by the callable.

    Arguments:
        func (callable): a function in which the exception is silenced
        x (anything): any variable that the callable requires
        exceptions (iterable, optional):
            list of exceptions that are to be caught.
            Default case catches Exception in general.
            It is advisable to passspecific exceptions.
        fail (bool, optional):
            Returns a bool depending on whether one wants to fail the rules
            or not, since even one failure will cause an object skip.
            This is the default behavior.
    """
    try:
        func(x)
    except:
        return not fail
