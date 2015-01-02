class NoValidationError(Exception):
    """
    This raises an exception when validations are expected but none have been
    specified.

    Attributes:
        obj -- object on which the validations were expected
        message -- message to pass for this event
    """
    def __init__(self, obj, message=None):
        self.obj = obj
        if not message:
            self.message = "Validation rules were expected for {}".format(obj)
        else:
            self.message = message
