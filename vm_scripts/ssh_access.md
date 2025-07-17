# 🔐 SSH Access to Tenant Containers

1. Get container IP address:
```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' tenant3

ssh tenant3@<ip_address>


Optional: You can use Docker networks to enable inter-container SSH (if needed).

6. tenant_template.env (optional)

If you want to use .env files for future automation, you can add something like:

```env
TENANT=tenant1/2/3
PASSWORD=tenant@123
IMAGE=tenant1-image
VOLUME=/mnt/tenant3-secure
