import base64

def xor_encrypt(message, key):
    key = key.encode("utf-8")
    msg = message.encode("utf-8")
    out = bytes([m ^ key[i % len(key)] for i, m in enumerate(msg)])
    return base64.b64encode(out).decode("utf-8")

def xor_decrypt(cipher, key):
    key = key.encode("utf-8")
    data = base64.b64decode(cipher)
    out = bytes([c ^ key[i % len(key)] for i, c in enumerate(data)])
    return out.decode("utf-8")

clé = "pomme"
message = "Bonjour, comment ça va toi"
cipher = xor_encrypt(message, clé)
print("Ciphertext:", cipher)
decrypted_message = xor_decrypt(cipher, clé)
print("Decrypted message:", decrypted_message)