
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac, serialization
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF


# DHandEncrypt function takes 3 inputs:
# A's private key,
# B's private key,
# plaintext that needs to be encrypted.

def DHandEncrypt(A_Private_Key, B_Private_Key, Plaintext):

    # mybackend is assigned the value returned by default_backend()
    mybackend = default_backend()

    # Load private keys of A and B
    private_key_A = serialization.load_pem_private_key(
        A_Private_Key, None, mybackend)
    private_key_B = serialization.load_pem_private_key(
        B_Private_Key, None, mybackend)

    # Perform Diffie-Hellman key exchange
    diffieH_A = private_key_A.exchange(private_key_B.public_key())
    diffieH_B = private_key_B.exchange(private_key_A.public_key())

    # Derive the shared key
    sharedAB_key2 = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'handshake data',
        backend=mybackend
    ).derive(diffieH_A + diffieH_B)

    # Encrypt the plaintext using XOR and the shared key
    ciphertext = bytearray(len(Plaintext))
    for i in range(len(Plaintext)):
        ciphertext[i] = Plaintext[i] ^ sharedAB_key2[i % 32]

    return sharedAB_key2, bytes(ciphertext)


if __name__ == "__main__":
    A_PRIVATE_KEY = b'-----BEGIN PRIVATE KEY-----\nMIGcAgEAMFMGCSqGSIb3DQEDATBGAkEAlry2DwPC+pK/0QiOicVAtt6ANsfjmD9P\nQrDC6ZkYcrRf0q0RVzMDTnHWk1mRLVvb6av4HOSkIsk1mMogBcqV0wIBAgRCAkBm\nZK4qUqvU6WaPy4fNG9oWIXchxzztxmA7p9BFXbMzn3rHcW84SDwTWXAjkRd35XPV\n/9RAl06sv191BNFFPyg0\n-----END PRIVATE KEY-----\n'

    B_PRIVATE_KEY = b'-----BEGIN PRIVATE KEY-----\nMIGcAgEAMFMGCSqGSIb3DQEDATBGAkEAlry2DwPC+pK/0QiOicVAtt6ANsfjmD9P\nQrDC6ZkYcrRf0q0RVzMDTnHWk1mRLVvb6av4HOSkIsk1mMogBcqV0wIBAgRCAkBn\n9zn/q8GMs7SJjZ+VLlPG89bB83Cn1kDRmGEdUQF3OSZWIdMAVJb1/xaR4NAhlRya\n7jZHBW5DlUF5rrmecN4A\n-----END PRIVATE KEY-----\n'

    PlainText = b"Encrypt me with the derived key!"

    STD_KEY, STD_CIPHER = DHandEncrypt(A_PRIVATE_KEY, B_PRIVATE_KEY, PlainText)
    print("Shared Key: ", STD_KEY)
    print("Ciphertext: ", STD_CIPHER)
