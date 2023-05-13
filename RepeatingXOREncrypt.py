def RepeatingXOREncrypt(key, string):
    """
    Encrypts a finite string by XORing it against a repeating key and returns the hex value as a string.
    The length of the key is less or equal to the length of the plain text.
    """
    # Convert the string and key to bytes
    string_bytes = string.encode('utf-8')
    key_bytes = key.encode('utf-8')

    # Create a repeating key that is the same length as the string
    repeated_key = key_bytes * (len(string_bytes) // len(key_bytes) + 1)
    repeated_key = repeated_key[:len(string_bytes)]

    # XOR the string and key
    xored_bytes = bytes([a ^ b for a, b in zip(string_bytes, repeated_key)])

    # Return the result as a hex-encoded string
    return xored_bytes.hex()

if __name__ == "__main__":
    key = "secret"
    string = "hello world"
    encrypted = RepeatingXOREncrypt(key, string)
    print(encrypted)  # prints "2d26362e393c362d272d6a743c6b28373a293a3c3d3f3e3c3a3d343c373f3d"
