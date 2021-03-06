#  vim: set fileencoding:utf-8 :

# Copyright (c) 2018 Yubico AB
# All rights reserved.
#
#   Redistribution and use in source and binary forms, with or
#   without modification, are permitted provided that the following
#   conditions are met:
#
#    1. Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#    2. Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following
#       disclaimer in the documentation and/or other materials provided
#       with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from __future__ import unicode_literals


"""Scancode map for BÉPO (fr dvorak) keyboard layout"""

SHIFT = 0x80

scancodes = {
    '\t': 0x2b | SHIFT,
    '\n': 0x28 | SHIFT,
    ' ': 0x2c,
    '!': 0x1c | SHIFT,
    '"': 0x1e,
    '#': 0x35 | SHIFT,
    '$': 0x35,
    '%': 0x2e,
    "'": 0x11,
    '(': 0x21,
    ')': 0x22,
    '*': 0x27,
    '+': 0x24,
    ',': 0x0a,
    '-': 0x25,
    '.': 0x19,
    '/': 0x26,
    '0': 0x27 | SHIFT,
    '1': 0x1e | SHIFT,
    '2': 0x1f | SHIFT,
    '3': 0x20 | SHIFT,
    '4': 0x21 | SHIFT,
    '5': 0x22 | SHIFT,
    '6': 0x23 | SHIFT,
    '7': 0x24 | SHIFT,
    '8': 0x25 | SHIFT,
    '9': 0x26 | SHIFT,
    ':': 0x19 | SHIFT,
    ';': 0x0a | SHIFT,
    '=': 0x2d,
    '?': 0x11 | SHIFT,
    '@': 0x23,
    'A': 0x04 | SHIFT,
    'B': 0x14 | SHIFT,
    'C': 0x0b | SHIFT,
    'D': 0x0c | SHIFT,
    'E': 0x09 | SHIFT,
    'F': 0x38 | SHIFT,
    'G': 0x36 | SHIFT,
    'H': 0x37 | SHIFT,
    'I': 0x07 | SHIFT,
    'J': 0x13 | SHIFT,
    'K': 0x05 | SHIFT,
    'L': 0x12 | SHIFT,
    'M': 0x34 | SHIFT,
    'N': 0x33 | SHIFT,
    'O': 0x15 | SHIFT,
    'P': 0x08 | SHIFT,
    'Q': 0x10 | SHIFT,
    'R': 0x0f | SHIFT,
    'S': 0x0e | SHIFT,
    'T': 0x0d | SHIFT,
    'U': 0x16 | SHIFT,
    'V': 0x18 | SHIFT,
    'W': 0x30 | SHIFT,
    'X': 0x06 | SHIFT,
    'Y': 0x1b | SHIFT,
    'Z': 0x2f | SHIFT,
    '`': 0x2e | SHIFT,
    'a': 0x04,
    'b': 0x14,
    'c': 0x0b,
    'd': 0x0c,
    'e': 0x09,
    'f': 0x38,
    'g': 0x36,
    'h': 0x37,
    'i': 0x07,
    'j': 0x13,
    'k': 0x05,
    'l': 0x12,
    'm': 0x34,
    'n': 0x33,
    'o': 0x15,
    'p': 0x08,
    'q': 0x10,
    'r': 0x0f,
    's': 0x0e,
    't': 0x0d,
    'u': 0x16,
    'v': 0x18,
    'w': 0x30,
    'x': 0x06,
    'y': 0x1b,
    'z': 0x2f,
    '\xa0': 0x2c | SHIFT,
    '«': 0x1f,
    '°': 0x2d | SHIFT,
    '»': 0x20,
    'À': 0x1d | SHIFT,
    'Ç': 0x31 | SHIFT,
    'È': 0x17 | SHIFT,
    'É': 0x1a | SHIFT,
    'Ê': 0x64 | SHIFT,
    'à': 0x1d,
    'ç': 0x31,
    'è': 0x17,
    'é': 0x1a,
    'ê': 0x64
}
