import passlib.hash
import sys

if len(sys.argv)<2:
    exit(1)

string = sys.argv[1]

print(passlib.hash.sha1_crypt.hash(string))