#!/bin/bash

TENANT=$1
if [ -z "$TENANT" ]; then
  echo "Usage: ./build_image.sh tenant-name"
  exit 1
fi

echo "📦 Building Docker image for $TENANT..."
docker build -t ${TENANT}-image --build-arg USERNAME=$TENANT -f Dockerfile .
