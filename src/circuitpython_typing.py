# The MIT License (MIT)
#
# Copyright (c) 2017 cefn for adafruit industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`circuitpython_typing` - Define subset of types for C-level protocols
=====================================================================

See `CircuitPython:circuitpython_typing` in CircuitPython for more details.

* Author(s): Alec Delaney
"""

from typing import Union
from array import array

ReadableBuffer = Union[bytes, bytearray, memoryview, array]
"""Classes that implement the readable buffer protocol

  * `bytes`
  * `bytearray`
  * `memoryview`
  * `array.array`
"""

WriteableBuffer = Union[bytearray, memoryview, array]
"""Classes that implement the writeable buffer protocol

  * `bytearray`
  * `memoryview`
  * `array.array`
"""