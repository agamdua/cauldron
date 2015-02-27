"""
Utils that assume what you are doing

(Here be dragons)
"""


def silence(func, x, exceptions=Exception, fail=False, ret=False):
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
        if ret:
            # TODO: Refactor and move out into its own function,
            # really does not belong here.
            return func(x)
        else:
            return bool(func(x))
    except exceptions:
        return not fail
