#!/bin/bash
set -e

while ! pg_isready -U "postgres"; do
    echo "Waiting for PostgreSQL to start..."
    sleep 5
done

# PostgreSQL 데이터베이스 생성
psql -U postgres -c "\l" | grep "$DB_NAME" &> /dev/null
if [ $? -eq 0 ]; then
    echo "Database '$DB_NAME' exists."
else
    echo "Database '$DB_NAME' does not exist."
	psql -U postgres -c "CREATE DATABASE $DB_NAME;"
fi

# 사용자 생성
psql -U postgres -c "\du" | grep "$DB_USER" &> /dev/null
if [ $? -eq 0 ]; then
    echo "User '$DB_USER' exists."
else
    echo "User '$DB_USER' does not exist."
	psql -U postgres -c "CREATE USER $DB_USER WITH ENCRYPTED PASSWORD '$DB_USER_PASSWORD';"
	psql -U postgres -c "ALTER DATABASE $DB_NAME OWNER TO $DB_USER;"
fi
