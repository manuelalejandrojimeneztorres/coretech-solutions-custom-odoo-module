#!/usr/bin/env bash
set -euo pipefail

# Variables
PROJECT_ROOT="$(dirname "$(realpath "$0")")"
BACKUP_DIR="${PROJECT_ROOT}/backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="backup_${TIMESTAMP}.sql.gz"
CONTAINER_NAME="odoo_postgres"  # Change to the actual container name

# Ensure required environment variables are set
: "${POSTGRES_USER:?Environment variable POSTGRES_USER is not set.}"
: "${POSTGRES_DB:?Environment variable POSTGRES_DB is not set.}"

# Create the backup directory if it does not exist
mkdir -p "${BACKUP_DIR}"

# Perform the database backup
log_message() {
    echo -e "[INFO] $1"
}

log_message "Starting database backup..."
if docker exec "${CONTAINER_NAME}" pg_dump -U "${POSTGRES_USER}" "${POSTGRES_DB}" | gzip > "${BACKUP_DIR}/${BACKUP_NAME}"; then
    log_message "Backup created successfully: ${BACKUP_DIR}/${BACKUP_NAME}"
else
    log_message "Backup failed. Please check the logs for more details."
    exit 1
fi
