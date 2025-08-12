import requests
import base64
import os

KMS_URL = "http://192.168.133.130:5000"  # Replace <host-ip> with actual host IP

def fetch_keys():
    print(" ^=^t^p Requesting RSA key pair from KMS...")
    try:
        res = requests.post(f"{KMS_URL}/generate_keys")
        keys = res.json()
        with open("public.pem", "w") as pub_file:
            pub_file.write(keys["public_key"])
        with open("private.pem", "w") as priv_file:
            priv_file.write(keys["private_key"])
        print(" ^|^e Keys saved: public.pem, private.pem")
    except Exception as e:
        print(f" ^}^l Failed to fetch keys: {e}")
        exit(1)

def encrypt_file(file_path):
    with open(file_path, "r") as f:
        message = f.read()
    with open("public.pem", "r") as f:
        public_key = f.read()

    print(f" ^=^t^p Encrypting {file_path}...")

    try:
              res = requests.post(f"{KMS_URL}/encrypt", json={
            "public_key": public_key,
            "message": message
        })
        encrypted = res.json()["encrypted_message"]
        enc_file = f"{file_path}.enc"
        with open(enc_file, "w") as f:
            f.write(encrypted)
        print(f" ^|^e Encrypted data saved to {enc_file}")
        return enc_file
    except Exception as e:
        print(f" ^}^l Encryption failed: {e}")
        exit(1)

def decrypt_file(enc_file_path):
    with open(enc_file_path, "r") as f:
        encrypted_data = f.read()
    with open("private.pem", "r") as f:
        private_key = f.read()

    print(f" ^=^t^s Decrypting {enc_file_path}...")

    try:
        res = requests.post(f"{KMS_URL}/decrypt", json={
            "private_key": private_key,
            "encrypted_message": encrypted_data
        })
        decrypted = res.json()["decrypted_message"]
        dec_file = enc_file_path.replace(".enc", ".dec.txt")
        with open(dec_file, "w") as f:
            f.write(decrypted)
        print(f" ^|^e Decrypted data saved to {dec_file}")
    except Exception as e:
        print(f" ^}^l Decryption failed: {e}")
        exit(1)

if __name__ == "__main__":
    original_file = "tenant1_data.txt"  # This should exist in /mnt/secure
    if not os.path.exists(original_file):
        print(f" ^}^l File '{original_file}' not found in /mnt/secure. Please create it first.")
        exit(1)

    fetch_keys()
    enc_file = encrypt_file(original_file)
    decrypt_file(enc_file)

        res = requests.post(f"{KMS_URL}/encrypt", json={
