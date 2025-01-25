#!/usr/bin/env bash
set -euo pipefail

# Define the project root directory
PROJECT_ROOT="$(dirname "$(realpath "$0")")"

# Ensure we are in the project root
cd "$PROJECT_ROOT"

# Function to log messages
log_message() {
    echo -e "[INFO] $1"
}

# Stop all services defined in docker-compose.yml
log_message "Stopping all containers..."
docker-compose down

# Remove orphan containers, if any
log_message "Removing orphan containers (if any)..."
docker-compose down --remove-orphans

log_message "All containers stopped successfully."
