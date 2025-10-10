Identify the Python version and bytecode number (in decimal, not hex) for as many of the bytecode files in this directory you can do.

``pydisasm -F header *name*`` can help here. Or

```
import sys, struct;
with open(sys.argv[1], "rb") as fp:
   print(struct.unpack("<H", fp.read(2))[0])
```
And there are other ways.

Places where you can get a map of integer magic number to Python version:

* https://github.com/rocky/python-xdis/blob/master/xdis/magics.py#L134-L649
* https://github.com/python/cpython/blob/dea7e3d5f8a63bc8883ca2874ab37c4587e85cda/Lib/importlib/_bootstrap_external.py#L226-L454
* https://github.com/python/cpython/blob/main/PC/launcher.c#L1250-L1277

1. Do the Bytecode versions always increase? If not, give a specific example.

2. What are the different kinds of platforms for Python aside from CPython?

3. Are the bytecode numbers the same for a CPython 3.11 interpreter versus a PyPy 3.11 interpreter?

4. Are there any Python's that use the same number as CPython but are different implementations, i.e. do not declare themselves as CPython?

5. What Python version is associated with 3420?

6. Which Pythons do not appear to use Python-like or Python-based bytecode?
