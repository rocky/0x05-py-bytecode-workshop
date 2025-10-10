Disassembly
-----------

1. Disassemble or decompile the five$py.class which was created in Jython 2.7.4 . It source the five.py program.
Hint: use a java decompiler.

2. Graal-24.2.2 *Python 3.11.7 uses JVM bytecode the `co_code` field of it `co_object`.
It extends the 3.11 code type with some additional fields:

* `co_lines`
* `co_lnotab` (compatible with 3.10)
* `co_positions`

Extend the disassembler for this.

3a. Extend the disassembler to handle RustPython.

3b. After this is done see if this can be hooked into pylingual.

Pylingual
---------

1. Extend Pylingual so that it handles one of the PyPy variants for 3.6-3.11. Pydisasm from xdis already supports PyPy.


Assembler project
-----------------

1. pyc-xasm does not write bytecode files properly on CPython 3.11 and newer. The Python Code structure has changed again: fields `co_localsplusnames` and `co->co_localspluskinds` were added and field `co_nlocals` was removed. Fix xdis so that it writes proper Python 3.11 pyc files. (Some code in xdis has been adjusted for the CPython code type.)



Decompilation
-------------

1. Investigate writing a decompiler for Ethereum EVM to Solidity. There are disassemblers for EVM. There is also a pyenv for switching Solidity compiltions.

2. Investigate detecting specific idioms in compiled languages, as a means for improving decompilers in compiled languages.

General Programming
-------------------

Find, Report and possibly fix any of the bugs you find in my code.
