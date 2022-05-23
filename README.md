# Sentinels

This is a reference implementation of a utility for the definition of
sentinel values in Python.  This also includes a [draft PEP](pep-0661.rst) for
the inclusion of this utility in the Python standard library.

## Usage

```python
from sentinels import Sentinel

NotGiven = Sentinel('NotGiven')
```

## References

* [Discussion on the python-dev mailing list](https://mail.python.org/archives/list/python-dev@python.org/thread/ZLVPD2OISI7M4POMTR2FCQTE6TPMPTO3/)
* [Poll and additional discussion on discuss.python.org](https://discuss.python.org/t/sentinel-values-in-the-stdlib/8810)
