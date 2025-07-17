#!/bin/bash

TENANT=$1
if [ -z "$TENANT" ]; then
  echo "Usage: ./create_tenants.sh tenant-name"
  exit 1
fi

IMAGE_NAME="${TENANT}-image"
CONTAINER_NAME="$TENANT"
HOSTNAME="$TENANT-host"
VOLUME_PATH="/mnt/${TENANT}-secure"

echo "🚀 Creating container: $CONTAINER_NAME"
docker run -dit \
  --name "$CONTAINER_NAME" \
  --hostname "$HOSTNAME" \
  -v "$VOLUME_PATH:/mnt/secure" \
  --cap-add=SYS_ADMIN \
  --cap-add=NET_ADMIN \
  "$IMAGE_NAME"

  
