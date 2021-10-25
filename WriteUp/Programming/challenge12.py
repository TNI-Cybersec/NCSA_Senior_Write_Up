# flag = "REDACTED"
flag = "NCSA{1d114185ec1737e6854d6a36734aad1b}"

def super_encode(flag):
    old = 0
    out = []
    for f in flag:
        new = (ord(f) + old) % 256
        out.append(new)
        old = ord(f)

    return out

secret = super_encode(flag)
print(secret)

secret = [71, 150, 111, 103, 150, 111, 110, 145, 150, 148, 188, 172, 149, 149, 98, 101, 101, 105, 109, 154, 200, 148, 104, 106, 106, 156, 155, 110, 109, 105, 152, 154, 151, 148, 105, 109, 106, 103, 149, 194, 197, 149, 147, 223, 157, 103, 150, 111, 103, 150]

def super_decode(secret,n=0):
    i = 0
    old = 0
    out = []
    if n ==0:
        for x in secret:
            old = (x-old)%256
            out.append(old)
        return out
    else:
        while True:
            for x in range(256):
                if (x + old) % 256 == secret[i]:
                    out.append(x)
                    old = x
                    i+=1
                    break
            if i >= len(secret):
                return out

plain = super_decode(secret)
print(flag)
print("".join([chr(x) for x in plain]))
#plain = "GO GO NCSA{1d114185ec1737e6854d6a36734aad1b} GO GO"
