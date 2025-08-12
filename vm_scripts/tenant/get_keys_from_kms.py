import requests

def get_keys():
    response = requests.post("http://172.17.0.6:5000/generate_keys")
    keys = response.json()
    with open("public.pem", "w") as f:
        f.write(keys["public_key"])
    with open("private.pem", "w") as f:
        f.write(keys["private_key"])
    print("✔ Keys saved to public.pem and private.pem")

if __name__ == "__main__":
    get_keys()
