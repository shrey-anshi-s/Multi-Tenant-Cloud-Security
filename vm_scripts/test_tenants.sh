#!/bin/bash

TENANT=$1
if [ -z "$TENANT" ]; then
  echo "Usage: ./test_tenants.sh tenant-name"
  exit 1
fi

echo "📦 Accessing $TENANT container..."
docker exec -it $TENANT bash -c "
  echo '🤖 whoami:'; whoami;
  echo '🔁 Switching to user $TENANT...';
  su - $TENANT -c 'whoami && hostname'
"
