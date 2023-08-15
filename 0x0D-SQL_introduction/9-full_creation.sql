#!/bin/bash

# Get the database name from the command-line argument
db_name="$1"

# Define the SQL script
sql_script=$(cat <<EOF
CREATE TABLE IF NOT EXISTS ${db_name}.second_table (
    id INT PRIMARY KEY,
    name VARCHAR(256),
    score INT
);

INSERT INTO ${db_name}.second_table (id, name, score)
VALUES (1, 'John', 10), (2, 'Alex', 3), (3, 'Bob', 14), (4, 'George', 8);
EOF
)

# Execute the SQL script using MySQL command-line tool
mysql -u your_username -p your_password -e "${sql_script}"
