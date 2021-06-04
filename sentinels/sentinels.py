import sys as _sys
import threading as _threading


__all__ = ['sentinel']


if hasattr(_sys, '_getframe'):
    _get_parent_frame = lambda: _sys._getframe(2)
else:  #pragma: no cover
    def _get_parent_frame():
        """Return the frame object for the caller's parent stack frame."""
        try:
            raise Exception
        except Exception:
            return _sys.exc_info()[2].tb_frame.f_back.f_back


def _get_type_name():
    with _get_type_name.lock:
        _get_type_name.counter += 1
    return f'_sentinel_type_{_get_type_name.counter}_'
_get_type_name.counter = 0
_get_type_name.lock = _threading.Lock()


def sentinel(name, repr=None):
    """Create a unique sentinel object."""
    name = _sys.intern(str(name))
    repr = repr or f'<{name}>'

    class_name = _get_type_name()
    class_namespace = {
        '__repr__': lambda self: repr,
    }
    cls = type(class_name, (), class_namespace)
    cls.__module__ = __name__
    globals()[class_name] = cls

    sentinel = cls()

    def __new__(cls):
        return sentinel
    __new__.__qualname__ = f'{class_name}.__new__'
    cls.__new__ = __new__

    return sentinel
