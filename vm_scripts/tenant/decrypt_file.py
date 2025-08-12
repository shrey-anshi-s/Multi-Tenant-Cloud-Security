import requests
import base64

def decrypt_file(encrypted_path, private_key_path):
    with open(encrypted_path, "r") as f:
        encrypted = f.read()
    with open(private_key_path, "r") as f:
        private_key = f.read()

    res = requests.post("http://localhost:5000/decrypt", json={
        "private_key": private_key,
        "encrypted_message": encrypted
    })

    decrypted = res.json()["decrypted_message"]

    output_file = encrypted_path.replace(".enc", ".dec.txt")
    with open(output_file, "w") as f:
        f.write(decrypted)
    print(f"[✓] Decrypted content saved to {output_file}")

if __name__ == "__main__":
    decrypt_file("tenant1_data.txt.enc", "private.pem")
