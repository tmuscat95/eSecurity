from Crypto.Cipher import DES
import hashlib
import sys
import binascii
import Padding

def decrypt(ciphertext,key,mode):
	encobj = DES.new(key,mode)
	return encobj.decrypt(ciphertext)

if (len(sys.argv)>1):
        ciphertext=binascii.unhexlify(sys.argv[1])

if(len(sys.argv)>2):
        key=hashlib.sha256(sys.argv[2]).digest()[:8]


plaintext = decrypt(ciphertext,key,DES.MODE_ECB)

plaintext = Padding.removePadding(plaintext,blocksize=Padding.DES_blocksize,mode='CMS')

print plaintext

