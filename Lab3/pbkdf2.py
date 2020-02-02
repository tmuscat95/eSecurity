import passlib.hash
import sys

if len(sys.argv)<2:
    exit(1)

string = sys.argv[1]

if len(sys.argv)>2:
    salt = sys.argv[2]
else:
    salt = "ZDzPE45C"

salt = salt.encode('utf-8')
print(passlib.hash.pbkdf2_sha1.hash(string,salt=salt))
print(passlib.hash.pbkdf2_sha256.hash(string,salt=salt))