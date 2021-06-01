def sentinel(repr):
    """Class decorator for defining sentinel values.

    Usage:

    @sentinel(repr='<NotGiven>')
    class NotGivenType: pass
    NotGiven = NotGivenType()
    """
    # Bail if mistakenly used without providing a repr.
    assert isinstance(repr, str)

    def inner(cls):
        cls.__repr__ = lambda self: repr
        instance = cls()
        cls.__new__ = lambda cls: instance
        return cls

    return inner
