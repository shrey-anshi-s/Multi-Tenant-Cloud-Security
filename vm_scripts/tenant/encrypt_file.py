import requests
import base64

def encrypt_file(file_path, public_key_path):
    with open(file_path, "r") as f:
        data = f.read()
    with open(public_key_path, "r") as f:
        public_key = f.read()

    res = requests.post("http://localhost:5000/encrypt", json={
        "public_key": public_key,
        "message": data
    })

    encrypted = res.json()["encrypted_message"]

    with open(f"{file_path}.enc", "w") as f:
        f.write(encrypted)
    print(f"[✓] File encrypted and saved as {file_path}.enc")

if __name__ == "__main__":
    encrypt_file("tenant1_data.txt", "public.pem")
