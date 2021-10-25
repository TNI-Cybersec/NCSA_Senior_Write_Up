#!/usr/bin/env python3

#flag = b'REDACTED'
flag = 'NCSA{45d20b1d2cc2d52e74b3cbf1750a2e31}'

def enc(plaintext):
    out = []
    for c in plaintext:
        h = (int(ord(c) & 0xF0) >> 4) - 2
        l = (int(ord(c) & 0x0F) + 1) << 4
        o = int(h) + int(l)
        out.append(o)
    return out

ciphertext = enc(flag)
print(ciphertext)

ciphertext = b'UUUUUUUU\x10\xf2BC"\xc5QaT1\x114!T1DD1Ta1d\x81Q4AD4t!\x81a\x11$1dA!\xe5\x10UUUUUUUU'

def dec(plaintext):
    out = []
    for c in plaintext:
        h = (int(c & 0x0F) + 2) << 4
        l = (int(c & 0xF0) >> 4 ) - 1
        o = int(h) + int(l)
        out.append(o)
    return out

plaintext = dec(ciphertext)
print(flag)
print("".join([chr(x) for x in plaintext]))
# plaintext = b'tttttttt NCSA{45d20b1d2cc2d52e74b3cbf1750a2e31} tttttttt'
