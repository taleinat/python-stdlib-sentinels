import sys as _sys
from typing import Optional


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


def _get_type_name(
        sentinel_qualname: str,
        module_name: Optional[str] = None,
) -> str:
    return (
        '_sentinel_type__'
        f'{module_name.replace(".", "_") + "__" if module_name else ""}'
        f'{sentinel_qualname.replace(".", "_")}'
    )


def sentinel(
        name: str,
        repr: Optional[str] = None,
        module: Optional[str] = None,
):
    """Create a unique sentinel object."""
    name = _sys.intern(str(name))
    repr = repr or f'<{name}>'

    if module is None:
        try:
            module = _get_parent_frame().f_globals.get('__name__', '__main__')
        except (AttributeError, ValueError):
            pass
    class_name = _get_type_name(name, module)

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
