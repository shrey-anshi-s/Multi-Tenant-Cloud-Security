from flask import Flask, request, jsonify
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import base64

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "KVM Key API is running!"

@app.route('/generate_keys', methods=['POST'])
def generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ).decode()

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode()

    return jsonify({
        "private_key": private_pem,
        "public_key": public_pem
    })
@app.route('/encrypt', methods=['POST'])
def encrypt_message():
    data = request.get_json()
    public_key_pem = data.get('public_key')
    message = data.get('message')

    public_key = serialization.load_pem_public_key(public_key_pem.encode())
    encrypted = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    encrypted_b64 = base64.b64encode(encrypted).decode()
    return jsonify({"encrypted_message": encrypted_b64})

@app.route('/decrypt', methods=['POST'])
def decrypt_message():
    data = request.get_json()
    private_key_pem = data.get('private_key')
    encrypted_b64 = data.get('encrypted_message')

    private_key = serialization.load_pem_private_key(private_key_pem.encode(), password=None)
    encrypted_bytes = base64.b64decode(encrypted_b64)

    decrypted = private_key.decrypt(
              encrypted_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return jsonify({"decrypted_message": decrypted.decode()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
