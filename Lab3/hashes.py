import hashlib
import passlib.hash
import sys
import bcrypt

if len(sys.argv)<2:
    exit(1)

salt="ZDzPE45C"
string=sys.argv[1].encode("utf-8")
salt2="1111111111111111111111"

print("General Hashes")
print("MD5:"+hashlib.md5(string).hexdigest()) 
print("SHA1:"+hashlib.sha1(string).hexdigest()) 
print("SHA256:"+hashlib.sha256(string).hexdigest()) 
print("SHA512:"+hashlib.sha512(string).hexdigest())
print("UNIX hashes (with salt)")
print("DES:"+passlib.hash.des_crypt.hash(string, salt=salt[:2])) 
print("MD5:"+passlib.hash.md5_crypt.hash(string, salt=salt))
print("Sun MD5:"+passlib.hash.sun_md5_crypt.hash(string, salt=salt))
print("SHA1:"+passlib.hash.sha1_crypt.hash(string, salt=salt))
print("SHA256:"+passlib.hash.sha256_crypt.hash(string, salt=salt))
print("SHA512:"+passlib.hash.sha512_crypt.hash(string, salt=salt)) 
print("Bcrypt:"+passlib.hash.bcrypt.normhash(passlib.hash.bcrypt.hash(string, salt=salt2[:22])))
