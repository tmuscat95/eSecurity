var crypto = require("crypto");
var args = process.argv


if(args.length<4)
    process.exit(1);

ciphertext = new Buffer(args[2],"hex");
key = crypto.createHash("sha256").update(args[3]).digest()
console.log("Key:\t" + key.toString("hex"));

var cipher = crypto.createDecipheriv('rc4',key,'');
var plaintext = cipher.update(ciphertext,"hex","utf8");
console.log(plaintext)
