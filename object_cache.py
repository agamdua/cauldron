from .exceptions import NoValidationError


class ObjectCache(object):
    """
    Store for all the objects that satisfy rules
    """
    def __init__(self, rules=None):
        """
        Instantiate the object cache with whatever validation rules
        are required

        These will ideally be sourced from a `settings` file.

        :param rules: all validation rules for storage
        :default rules: None
        """
        self.rules = rules

    def validate(self):
        """
        This method needs to be overwritten to include any validations
        """
        raise NoValidationError
