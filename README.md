# Security-Exercises

## Repeating XOR Encrypt
This is an implementation of a function which encrypts a finite string by XORing it against a repeating key and returns the hex value as a string. The length of the key is less or equal to the length of the plaintext.

## Diffie-Hellman Encrypt
This is function demonstrates how users A and B use the Diffie-Hellman (DH) key exchange protocol to share a secret key and start encrypting data. It is assumed that users A and B agreed on some DH parameters and calculated their private keys. I used keys below for examples:

User's A private key (in PEM, no password protected):

b'-----BEGIN PRIVATE KEY-----
\nMIGcAgEAMFMGCSqGSIb3DQEDATBGAkEAlry2DwPC+pK/0QiOicVAtt6ANsfjmD9P\nQrDC6Zk
YcrRf0q0RVzMDTnHWk1mRLVvb6av4HOSkIsk1mMogBcqV0wIBAgRCAkBm\nZK4qUqvU6WaPy4fN
G9oWIXchxzztxmA7p9BFXbMzn3rHcW84SDwTWXAjkRd35XPV\n/9RAl06sv191BNFFPyg0\n---
--END PRIVATE KEY-----\n'


User's B private key (in PEM, no password protected):

b'-----BEGIN PRIVATE KEY-----
\nMIGcAgEAMFMGCSqGSIb3DQEDATBGAkEAlry2DwPC+pK/0QiOicVAtt6ANsfjmD9P\nQrDC6Zk
YcrRf0q0RVzMDTnHWk1mRLVvb6av4HOSkIsk1mMogBcqV0wIBAgRCAkBn\n9zn/q8GMs7SJjZ+V
LlPG89bB83Cn1kDRmGEdUQF3OSZWIdMAVJb1/xaR4NAhlRya\n7jZHBW5DlUF5rrmecN4A\n---
--END PRIVATE KEY-----\n'

## AES in CTR mode Encryption
The code defines a function called AES_CTR_Encrypt that encrypts a plaintext message using AES-CTR encryption mode. The function takes a hexadecimal string key representing the encryption key, another hexadecimal string nonce_counter representing the initial value of the nonce and counter used by CTR mode, and a plaintext message data represented as a byte string.

The function creates an AES-CTR cipher and encryptor using the key and nonce_counter. It then encrypts the data using the created encryptor and returns the resulting ciphertext.
