#!/usr/bin/env bash
set -euo pipefail

# Variables
PROJECT_ROOT="$(dirname "$(realpath "$0")")"
CONTAINER_NAME="odoo_postgres"  # Change to the actual container name
BACKUP_FILE="${1:-}"  # Backup file provided as a positional argument

# Ensure required environment variables are set
: "${POSTGRES_USER:?Environment variable POSTGRES_USER is not set.}"
: "${POSTGRES_DB:?Environment variable POSTGRES_DB is not set.}"

# Function to log messages
log_message() {
    echo -e "[INFO] $1"
}

# Validate that the backup file exists
if [[ -z "$BACKUP_FILE" || ! -f "$BACKUP_FILE" ]]; then
    echo "Usage: $0 <backup_file>"
    echo "Please provide a valid backup file to restore."
    exit 1
fi

# Restore the backup
log_message "Restoring database from backup: ${BACKUP_FILE}..."
if gunzip -c "${BACKUP_FILE}" | docker exec -i "${CONTAINER_NAME}" psql -U "${POSTGRES_USER}" "${POSTGRES_DB}"; then
    log_message "Database restored successfully."
else
    log_message "Restore failed. Please check the logs for more details."
    exit 1
fi
