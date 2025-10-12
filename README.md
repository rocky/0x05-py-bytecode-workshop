# Introduction

These are notes and links from the slides I will present.  I put these
together so you don't have to write information from the slides.  We
also have specific commands to type and links to other information
here.

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Introduction](#introduction)
- [Slide 3.2 Why Study Python Bytecode?](#slide-32-why-study-python-bytecode)
- [6.1 Getting Set up for the workshop.](#61-getting-set-up-for-the-workshop)
- [6.2 Python Installation via OS Package Install](#62-python-installation-via-os-package-install)
  - [GNU/Linux](#gnulinux)
  - [MacOS](#macos)
  - [MS Windows](#ms-windows)
- [6.3 Python Installation via Virtual Environment](#63-python-installation-via-virtual-environment)
  - [virtualenv](#virtualenv)
  - [pyenv](#pyenv)
  - [pyenv-win](#pyenv-win)
- [6.4 Software we will be using today](#64-software-we-will-be-using-today)
  - [Versions of software](#versions-of-software)
- [6.5 Optional programs](#65-optional-programs)
- [7.1 Python Bytecode](#71-python-bytecode)
- [7.3 Magic number identification locations](#73-magic-number-identification-locations)
- [7.4 Python Identification Exercises](#74-python-identification-exercises)
- [10.1 Python Interpreter vs. C Static Compile](#101-python-interpreter-vs-c-static-compile)
- [13.2 Tracing Python Bytecode](#132-tracing-python-bytecode)
- [14.3 trepan-xpy on Python Bytecode](#143-trepan-xpy-on-python-bytecode)
- [15.1 trepan3k: a debugger that can debug without source](#151-trepan3k-a-debugger-that-can-debug-without-source)
- [15.2 trepan3k: a debugger that can debug without source](#152-trepan3k-a-debugger-that-can-debug-without-source)
- [16.1 Modifiying Python Bytecode: pyc-xasm](#161-modifiying-python-bytecode-pyc-xasm)

<!-- markdown-toc end -->

# Slide 3.2 Why Study Python Bytecode?

High-level bytecode is attractive for malware writers, because:

* It is portable
* It is compact
* It is impervious to General-purpose binary analysis tools

# 6.1 Getting Set up for the workshop.

* Please join slack channel #0x05-py-bytecoe workshop.
* Once you have joined send the output from:

```shell-session
$ python -V
```

Also send:

```shell-session
$ python -c 'import sys; print(sys.version)'
```

# 6.2 Python Installation via OS Package Install

## GNU/Linux

On GNU/Linux one way to install is via use [snap](https://snapcraft.io/python3-alt)

On Ubuntu:

```shell-session
$ sudo apt install python3
```

On CentOS, Fedora, or RedHat:

```shell-session
$ sudo dnf install python3 # or try yum
```

On CentOS, Fedora, or RedHat:

```shell-session
$ sudo dnf install python3 # or try yum
```

## MacOS

```shell-session
$ brew install python3@3.13
```

## MS Windows

```shell-session
$ choco install python --version=3.12 --params '"/InstallDir:C:\Python313"'
```

# 6.3 Python Installation via Virtual Environment

## virtualenv

```shell-session
$ mkdir
$ cd BSides-2025-workshop
$ python -m venv
$ venv/bin/activate venv
```

## pyenv

```shell-session
$ cd BSides-2025-workshop
$ curl https://pyenv.run | bash
$ pyenv install 3.13
$ # Follow instructions at: https://github.com/pyenv/pyenv#b-set-up-your-shell-environment-for-pyenv
```

## pyenv-win

```shell-session
$ Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
```

# 6.4 Software we will be using today


* [xdis](https://pypi.org/project/xdis/): 6.1.7
* [uncompyle6](https://pypi.org/project/uncompyle6/): 3.9.4
* [x-python](https://pypi.org/project/x-python/): 3.9.4
* [trepanxpy](https://pypi.org/project/trepanxpy/) 1.1.2
* [trepan3k](https://pypi.org/project/trepan3k/)
* [xasm](https://pypi.org/project/xasm/) 1.2.1
* control-flow &mdash; 1.0.0.alpha0

To install these:

```shell-session
$ pip install -r requirements-basic.txt
```

# 6.5 Optional programs

* [pycdc](https://github/zrax/pycdc/) (optional); can be installed via snap
* [pylingual](https://github.com/syssec-utd/pylingual) # can use from website http://pylingual.io

# 7.1 Python Bytecode

Simple Python source text (file `five.py`)

```python
def five():
    return "5"
```

Contents of Python 3.13 bytecode file using

```
python
import py_compile; py_compile("five,py", "five.cpython-313.pyc", "exec")
```

```
00000000: f30d 0d0a 0000 0000 cfed c168 2700 0000  ...........h'...
00000010: e300 0000 0000 0000 0000 0000 0004 0000  ................
00000020: 0000 0000 00f3 2400 0000 9500 5300 1a00  ......$.....S...
00000030: 7200 5c01 2200 5c00 2200 3500 0000 0000  r.\.".\.".5.....
00000040: 0000 3501 0000 0000 0000 2000 6701 2902  ..5....... .g.).
00000050: 6300 0000 0000 0000 0000 0000 0001 0000  c...............
00000060: 0003 0000 00f3 0400 0000 9500 6701 2902  ............g.).
00000070: 4ee9 0500 0000 a900 7204 0000 00f3 0000  N.......r.......
00000080: 0000 da07 6669 7665 2e70 79da 0466 6976  ....five.py..fiv
00000090: 6572 0700 0000 0100 0000 7305 0000 0080  er........s.....
000000a0: 00d8 0b0c 7205 0000 004e 2902 7207 0000  ....r....N).r...
000000b0: 00da 0570 7269 6e74 7204 0000 0072 0500  ...printr....r..
000000c0: 0000 7206 0000 00da 083c 6d6f 6475 6c65  ..r......&lt;module
000000d0: 3e72 0900 0000 0100 0000 7313 0000 00f0  &gt;r........s.....
000000e0: 0301 0101 f202 0101 0de1 0005 8164 8366  .............d.f
000000f0: 850d 7205 0000 00                        s........
```

# 7.3 Magic number identification locations

You can find a correspondence between magic number and its Python version here:

* https://github.com/rocky/python-xdis/blob/master/xdis/magics.py#L134-L649
* https://github.com/python/cpython/blob/dea7e3d5f8a63bc8883ca2874ab37c4587e85cda/Lib/importlib/_bootstrap_external.py#L226-L454
* https://github.com/python/cpython/blob/main/PC/launcher.c#L1250-L1277

Note: older CPython source code has this information elsewhere, so use the information from xdis.


# 7.4 Python Identification Exercises

Command to get header:

```
pydisasm --format header five-a.pyc
```

Which essentially does:

```
import sys, struct;
fp = open(sys.argv[1], "rb")
print(struct.unpack("<H", fp.read(2))[0])
```

# 10.1 Python Interpreter vs. C Static Compile

```python
def five():
    return 5
print(five()
```

```C
#include <stdio.h>
int five() {
  return 5;
}
int main(int argc, const char ** argv) {
  printf("%d\n", five());
}
```

Python Bytecode 3.13 Disassembly of main body:

```
...
# Constants:
#    0: <code object five at 0x78c311902a70, file "five.py", line 1>;
#    1: None
# Names:
#    0: five, 1: print
  0           RESUME                   0
  1           LOAD_CONST               (<code object five>)
              MAKE_FUNCTION
              STORE_NAME               (five)
  3           LOAD_NAME                (print)
              PUSH_NULL
              LOAD_NAME                (five)
              PUSH_NULL
              CALL                     (0 positional)
              CALL                     (1 positional)
              POP_TOP
              RETURN_CONST             (None)
```

LLVM disassembly of main body:

```llvm
Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @main(i32 noundef %0, ptr noundef %1) #0 {
  %3 = alloca i32, align 4
  %4 = alloca ptr, align 8
  store i32 %0, ptr %3, align 4
  store ptr %1, ptr %4, align 8
  %5 = call i32 @five()
  %6 = call i32 (ptr, ...) @printf(ptr noundef @.str, i32 noundef %5)
  ret i32 0
}
```

# 13.2 Tracing Python Bytecode

```shell-session
$ xpython -v 12-decompilation-examples/example6.pyc
```

![x-python trace of example6.pyc](13-xpython/example6.gif)

# 14.3 trepan-xpy on Python Bytecode (via source)

```shell-session
$ trepan-xpy 14-xpython/stack-example.py
```

![trepan-xpy demo run on stack-example](14-xpython/stack-example.gif)

Commands used:

* `list`: list source code
* `eval`: evaluate an expression (also `print`)
* `info block`: show block stack
* `info stack`: show evaluation stack
* `step`: step a bytecode instruction
* `backtrace`: show callframe stack
* `continue`: continue execution.


# 15.1 trepan3k: a debugger that can debug without source (and decompile)

```
pyenv local 3.8   # Set up to use a CPython 3.8 interpreter
trepan3k 15-bytecode-versions/five-c.pyc
```

![trepan-3k demo with embedded decompilation](15-trepan3k/trepan3k-example1.gif)


Commands used:

* `deparse`: deparse source text around stopped instruction offset
* `print`: evaluate an expression (also `eval`)
* `step`: step a bytecode instruction
* `backtrace`: show callframe stack
* `continue`: continue execution.


# 15.2 trepan3k: a debugger that can debug without source, disassembly only

```shell-session
$ pyenv local 3.13  # Set up to run a CPython 3.13 interpreter
$ trepan3k bytecode-versions/five-f.pyc
```

![trepan-3k demo with disassembly only](15-trepan3k/trepan3k-example2.gif)


Commands used in addition to those already mentioned:

* `set autopc`: show disassembly around stopped instruction offset

# 16.1 Modifiying Python Bytecode: pyc-xasm

The format `-F xasm` on `pydisasm` gives Bytecode assembly in text format.

```
$ pydisasm -F xasm assembling/example1.cpython-310.pyc > assembling/example1.xasm
```

You can then modify this and then create a Python bycode file using `pyx-xasm` from the `xasm` package.

We'll patch out a comparison test on getting the right "password", by
changing some opcodes to NOP (no operation) instructions.

```shell-session
$ cat assembling/example1-xasm.diff
$ patch -p1 assembling/example1-xasm.diff
```

Now assembly the using `pyc-xasm`:

```shell-session
$ pyc-xasm assembling/example1.xasm
```

And using a CPython 3.10 interpreter, or x-python: run the program:

```shell-session
$ python assembling/example1.pyc
$ x-python assembling/example1.pyc
```
