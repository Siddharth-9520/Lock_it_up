# rsa_utils.py
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import os

# Always locate the folder this file is in
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    with open(os.path.join(BASE_DIR, "private.pem"), "wb") as f:
        f.write(private_key)
    with open(os.path.join(BASE_DIR, "public.pem"), "wb") as f:
        f.write(public_key)
    print("* RSA Keys generated successfully! *")

def load_keys():
    with open(os.path.join(BASE_DIR, "private.pem"), "rb") as f:
        private_key = RSA.import_key(f.read())
    with open(os.path.join(BASE_DIR, "public.pem"), "rb") as f:
        public_key = RSA.import_key(f.read())
    return private_key, public_key

def encrypt_message(message, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    encrypted = cipher.encrypt(message.encode())
    return base64.b64encode(encrypted).decode()

def decrypt_message(encrypted_message, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    decrypted = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted.decode()
