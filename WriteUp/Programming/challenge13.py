import os

# flag = "REDACTED"
flag = "NCSA{373d338b7afcc450d4869d8a414aa767}"

def super_encode(flag):
    old = sum(os.urandom(8))
    out = []
    for f in flag:
        new = (ord(f) - old) % 256
        out.append(new)
        old = ord(f)
    return out

secret = super_encode(flag)
print(secret)
secret = super_encode(flag)
print(secret)

secret = [189, 20, 253, 187, 70, 6, 245, 6, 185, 73, 10, 173, 46, 245, 16, 238, 58, 184, 4, 252, 49, 207, 0, 5, 42, 213, 42, 5, 253, 0, 209, 1, 251, 52, 208, 4, 254, 3, 43, 212, 41, 211, 253, 3, 45, 0, 214, 255, 1, 70, 177, 242, 55, 14, 7, 0, 180, 36, 43, 255, 247]

def super_decode(secret,n=0):
    i = 0
    old = sum(os.urandom(8))
    out = []
    if n == 0:
        for x in secret:
            old = (x+old)%256
            out.append(old)
        return out
    else:
        while True:
            for x in range(256):
                if (x - old) % 256 == secret[i]:
                    out.append(x)
                    old = x
                    i+=1
                    break
            if i >= len(secret):
                return out

while True:
    plain = super_decode(secret)
    if "NCSA" in "".join([chr(x) for x in plain]):
        print(flag)
        print("".join([chr(x) for x in plain]))
        break
#plain = "The flag is NCSA{373d338b7afcc450d4869d8a414aa767}. Well Done"
