var chacha20 = require("chacha20");
var crypto = require("crypto");
var args = process.argv;

if(args.length<4)
    process.exit(1);

ciphertext = new Buffer.from(args[2],"hex");
key = args[3];

var nonce = new Buffer.alloc(8);
nonce.fill(0);

key = crypto.createHash("sha256").update(args[3]).digest()
console.log(key.toString("hex"));

plaintext = chacha20.decrypt(key,nonce,ciphertext);

console.log(plaintext.toString());