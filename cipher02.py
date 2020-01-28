from Crypto.Cipher import DES
import hashlib
import sys
import binascii
import Padding

if (len(sys.argv)>1):
	val=sys.argv[1]

if(len(sys.argv)>2):
	password=sys.argv[2]

plaintext=val

def encrypt(plaintext,key, mode):
	encobj = DES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = DES.new(key,mode)
	return(encobj.decrypt(ciphertext))

key = hashlib.sha256(password).digest()[:8]


plaintext = Padding.appendPadding(plaintext,blocksize=Padding.DES_blocksize,mode='CMS')
print "After padding (CMS): "+binascii.hexlify(bytearray(plaintext))

ciphertext = encrypt(plaintext,key,DES.MODE_ECB)
ciphertext
print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt(ciphertext,key,DES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,mode='CMS')
print "  decrypt: "+plaintext


plaintext=val


plaintext = Padding.appendPadding(plaintext,blocksize=Padding.DES_blocksize,mode='ZeroLen')
print "\nAfter padding (Bit): "+binascii.hexlify(bytearray(plaintext))

ciphertext = encrypt(plaintext,key,DES.MODE_ECB)
#print ciphertext
#print bytearray(ciphertext)
#print binascii.hexlify(ciphertext)
print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt(ciphertext,key,DES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,blocksize=Padding.DES_blocksize,mode='ZeroLen')
print "  decrypt: "+plaintext


plaintext=val

plaintext = Padding.appendPadding(plaintext,blocksize=Padding.DES_blocksize,mode='Space')
print "\nAfter padding (Null): "+binascii.hexlify(bytearray(plaintext))

ciphertext = encrypt(plaintext,key,DES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt(ciphertext,key,DES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,blocksize=Padding.DES_blocksize,mode='Space')
print "  decrypt: "+plaintext


plaintext=val

plaintext = Padding.appendPadding(plaintext,blocksize=Padding.DES_blocksize,mode='Random')
print "\nAfter padding (Random): "+binascii.hexlify(bytearray(plaintext))

ciphertext = encrypt(plaintext,key,DES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt(ciphertext,key,DES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,mode='Random')
print "  decrypt: "+plaintext
