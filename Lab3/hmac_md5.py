import sys
import base64
import hashlib
from hmac import *

if len(sys.argv)<3:
    exit(1)


h=HMAC(key=sys.argv[2].encode("utf-8"),msg=sys.argv[1].encode("utf-8"),digestmod=hashlib.md5)

oX=h.hexdigest()
b64= base64.b64encode(h.digest())
print(oX)
print(b64.decode("utf-8"))
