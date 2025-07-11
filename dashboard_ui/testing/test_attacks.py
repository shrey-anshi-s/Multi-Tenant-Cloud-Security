import requests

# URL of the target app
url = "http://127.0.0.1:5000"

# Simulated test: Try accessing another tenant's resource
def test_cross_tenant_access():
    payload = {"tenant_id": "other_tenant", "resource": "confidential_file"}
    resp = requests.post(f"{url}/access", json=payload)

    assert resp.status_code == 403, "Fail! Unauthorized access was allowed."

if __name__ == '__main__':
    test_cross_tenant_access()
    print("[TEST PASSED] Cross-Tenant Attack Simulation.")
