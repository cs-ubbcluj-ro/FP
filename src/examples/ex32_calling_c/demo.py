"""
Call fraction_value from a compiled C library.

Build once in this directory:
    macOS: cc -dynamiclib fraction.c -o libfraction.dylib
    Linux: cc -shared -fPIC fraction.c -o libfraction.so

Then run: python3 demo.py
"""

import ctypes
import sys
from pathlib import Path

library_name = "libfraction.dylib" if sys.platform == "darwin" else "libfraction.so"
library = ctypes.CDLL(str(Path(__file__).resolve().with_name(library_name)))

fraction_value = library.fraction_value
fraction_value.argtypes = [ctypes.c_int, ctypes.c_int]
fraction_value.restype = ctypes.c_double

if __name__ == "__main__":
    print(fraction_value(3, 2))
