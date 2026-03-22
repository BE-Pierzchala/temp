#!/bin/bash
# Save this as keep-docker-awake.sh and chmod +x it

while true; do
  if docker ps --format '{{.Names}}' | grep -q .; then
    # At least one container is running; prevent idle sleep
    echo "Containers running; Mac will not idle sleep..."
    caffeinate -i &
    CAFFEINE_PID=$!
    # Wait until containers stop
    while docker ps --format '{{.Names}}' | grep -q .; do
      sleep 10
    done
    kill $CAFFEINE_PID 2>/dev/null || true
  else
    sleep 10
  fi
done
