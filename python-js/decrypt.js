import forge from 'node-forge';
public_key.pem

const publicKey = forge.pki.publicKeyFromPem("public_key.pem");

var secretMessage = ;
var encrypted = publicKey.encrypt(secretMessage, "RSA-OAEP", {
    md: forge.md.sha256.create(),
    mgf1: forge.mgf1.create()
});
var base64 = forge.util.encode64(encrypted);