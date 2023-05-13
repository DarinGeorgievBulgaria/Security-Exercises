from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import struct

def AES_CTR_Encrypt(key, nonce_counter, data):
    
    # Converting the key and nonce_counter from hexadecimal to bytes
    key = bytes.fromhex(key)
    nonce_counter = bytes.fromhex(nonce_counter)

    # Creating the AES-ECB cipher and encryptor
    aesCipher = Cipher(algorithms.AES(key), modes.ECB(),backend=default_backend())
    aesEncryptor = aesCipher.encryptor()
    
    # Initializing the keystream as a bytearray
    keystream = bytearray()
    
    # For each block of 16 bytes in the data, encrypting the nonce_counter incremented by the block number 
    # using AES-ECB to obtain the keystream
    for i in range(0, len(data), 16):
        
        # Converting the nonce_counter to bytes and increment it by the block number
        
        blocknumber=(int.from_bytes(nonce_counter,byteorder='big')+i//      16).to_bytes(16,byteorder='big')
        # Updating the keystream with the encrypted block
        keystream += aesEncryptor.update(blocknumber)

    # XOR the data with the keystream to obtain the ciphertext
    ciphertext = bytearray(len(data))
    for i in range(len(data)):
        ciphertext[i] = data[i] ^ keystream[i]


#returning ciphertext as bytes
    return bytes(ciphertext)


if __name__ == "__main__":
    	key = '0000000000000000000000000000000000000000000000000000000000000001'
nonce_counter = '00000000000000000000000000000001'
data = b"12345678901234567890123456789012"
result = AES_CTR_Encrypt(key, nonce_counter, data)
print(result)

