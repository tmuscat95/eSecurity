from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding
import base64

def decrypt(ciphertext,key,mode):
	encobj = AES.new(key,mode)
	return encobj.decrypt(ciphertext)

if (len(sys.argv)>1):
	ciphertext = sys.argv[1]

if (len(sys.argv)>2):
	key=sys.argv[2]

if(len(sys.argv)>3):
	if(sys.argv[3]=="-base64"):
		ciphertext=base64.b64decode(ciphertext)

key=hashlib.sha256(key).digest()

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,blocksize=Padding.AES_blocksize,mode="CMS")

print plaintext
