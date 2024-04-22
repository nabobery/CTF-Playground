import string

def xor_decrypt(ciphertext, key):
    decrypted = b''
    for byte in ciphertext:
        decrypted += bytes([byte ^ key])
    return decrypted

def find_xor_key(ciphertext):
    for key in range(256):
        decrypted = xor_decrypt(ciphertext, key)
        if decrypted.startswith(b'SURGE{'):
            return key
    return None

ciphertext = bytes('F3PJJF5HVEYT3PAJLUHHKCMJSAPL5IHG2PSWEZHPBYEV64IC3WJU3P5F5CD6ULY', 'ascii') # replace <redacted> with the 65-character alphanumeric string
key = find_xor_key(ciphertext)
if key is not None:
    decrypted = xor_decrypt(ciphertext, key)
    flag = decrypted.decode()
    print(f'Flag: SURGE{flag}')
else:
    print('Could not find the XOR key')