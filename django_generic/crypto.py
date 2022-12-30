from cryptography.fernet import Fernet


def encrypt_url(url):
    # Generate a key
    key = Fernet.generate_key()
    fernet = Fernet(key)
    # Encrypt the URL
    encrypted_url = fernet.encrypt(url.encode())
    # Return the encrypted URL and the key
    return encrypted_url, key


def decrypt_url(encrypted_url, key):
    fernet = Fernet(key)
    # Decrypt the URL
    decrypted_url = fernet.decrypt(encrypted_url).decode()
    return decrypted_url
