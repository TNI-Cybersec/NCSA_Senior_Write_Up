# Challenge 10

สำหรับข้อนี้มี3แบบ

### แบบคนขยัน
```py
import re
filename = "challenge.txt"
pattern = ".{7}c.{7}a.{7}f.{7}e"
with open(filename) as file:
  for line in file:
      ln = line.rstrip()
      md5 = ln[ln.find('{') + 1:ln.find('}')]
      result = re.match(pattern, md5)
      if result:
          print(ln)
          break
```


### แบบคนธรรมดา
```py
with open(filename) as file:
  for line in file:
      ln = line.rstrip()
      md5 = ln[ln.find('{') + 1:ln.find('}')]
      if md5[7] == 'c' and md5[15] == 'a' and md5[23] == 'f' and md5[31] == 'e':
          print(ln)
          break
```

### แบบคนขี้เกียจ
```regex
RegEx = \.......c.......a.......f.......e\ หรือ \.{7}c.{7}a.{7}f.{7}e\
```
![Imgur](https://imgur.com/g2fnb4O.png)
![Imgur](https://imgur.com/sIR46fI.gif)

