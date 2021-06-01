import sys as _sys


if hasattr(_sys, '_getframe'):
    get_parent_frame = lambda: _sys._getframe(2)
else:  #pragma: no cover
    def get_parent_frame():
        """Return the frame object for the caller's parent stack frame."""
        try:
            raise Exception
        except Exception:
            return _sys.exc_info()[2].tb_frame.f_back.f_back


def sentinel(name, repr=None, module=None):
    """Create a unique sentinel object."""
    name = _sys.intern(str(name))
    repr = repr or f'<{name}>'

    # This is a hack to get copying and unpickling to work without setting the
    # class as a module attribute.
    class_name = f'{name}.__class__'
    class_namespace = {
        '__repr__': lambda self: repr,
    }
    cls = type(class_name, (), class_namespace)

    # For pickling to work, the class's __module__ variable needs to be set to
    # the name of the module where the sentinel is defined.
    if module is None:
        try:
            module = get_parent_frame().f_globals.get('__name__', '__main__')
        except (AttributeError, ValueError):
            pass
    if module is not None:
        cls.__module__ = module

    sentinel = cls()

    def __new__(self):
        return sentinel
    __new__.__qualname__ = f'{class_name}.__new__'
    cls.__new__ = __new__

    return sentinel
