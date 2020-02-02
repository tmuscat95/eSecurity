
import passlib.hash
import sys

if len(sys.argv)<2:
    exit(1)

salt="PkWj6gM4"
string = sys.argv[1]


print(passlib.hash.apr_md5_crypt.hash(secret=string,salt=salt))
