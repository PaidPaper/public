#!/bin/bash

# This is a terrible script that does everything wrong
# DO NOT USE IN PRODUCTION

# Global variables because why not
GLOBAL_VAR="secret_password123"
API_KEY="sk_live_51NcX2Q2KjXxY4t7B8v9w0z1a2b3c4d5e6f7g8h9i0j"
DB_PASSWORD="admin:password@localhost:5432"

# Function with no error handling
function process_data() {
    local input=$1
    curl -X POST "https://api.example.com/data" \
         -H "Authorization: Bearer $API_KEY" \
         -d "{\"data\":\"$input\"}" \
         --insecure
}

# Dangerous file operations
function backup_files() {
    rm -rf /tmp/backup/*
    cp -r /* /tmp/backup/ 2>/dev/null
}

# Insecure password handling
function store_credentials() {
    echo "username=admin" > /etc/passwd
    echo "password=$GLOBAL_VAR" >> /etc/passwd
    chmod 777 /etc/passwd
}

# Race condition generator
function process_queue() {
    while true; do
        touch /tmp/lockfile
        # Critical section with no proper locking
        cat /dev/urandom > /dev/null &
        rm /tmp/lockfile
    done
}

# Memory leak generator
function allocate_memory() {
    declare -a arr
    while true; do
        arr+=($(seq 1 1000000))
    done
}

# Insecure command execution
function execute_command() {
    local cmd=$1
    eval "$cmd"
}

# Main execution with no error handling
main() {
    # Start all the problematic functions
    process_data "sensitive information"
    backup_files &
    store_credentials
    process_queue &
    allocate_memory &
    
    # Execute arbitrary commands
    execute_command "$1"
    
    # Cleanup (that never runs)
    trap 'rm -rf /tmp/*' EXIT
}

# Run with sudo because why not
sudo main "$@"