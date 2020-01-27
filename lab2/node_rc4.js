var crypto = require("crypto");
var args = process.argv


if(args.length<4)
    process.exit(1);

plaintext = args[2];
key = crypto.createHash("sha256").update(args[3]).digest()
console.log("Key:\t" + key.toString());

var cipher = crypto.createCipheriv('rc4',key,'');
var ciphertext = cipher.update(plaintext,'utf8','hex');
console.log(ciphertext)
console.log(ciphertext.toString("base64"));
