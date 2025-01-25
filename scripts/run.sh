#!/usr/bin/env bash
set -euo pipefail

# Define the project root directory
PROJECT_ROOT="$(dirname "$(realpath "$0")")"
LOGS_DIR="$PROJECT_ROOT/logs"
DATA_DIR="$PROJECT_ROOT/data"

# Ensure we are in the project root
cd "$PROJECT_ROOT"

# Create required directories
mkdir -p "$LOGS_DIR" "$DATA_DIR"

# Adjust permissions securely
chmod 755 "$LOGS_DIR"

# Build and start containers
docker-compose up -d --build

# Log rotation settings
LOG_FILE="$LOGS_DIR/app.log"
MAX_SIZE=$((10 * 1024 * 1024)) # 10 MB

# Rotate logs if necessary
if [[ -f "$LOG_FILE" && $(stat -c%s "$LOG_FILE") -ge $MAX_SIZE ]]; then
    TIMESTAMP=$(date +"%Y%m%d%H%M%S")
    mv "$LOG_FILE" "$LOGS_DIR/app-$TIMESTAMP.log"
    touch "$LOG_FILE"
fi

# Append docker logs to the application log file
docker-compose logs -f >> "$LOG_FILE" &

echo "Odoo and PostgreSQL containers are up and running."
