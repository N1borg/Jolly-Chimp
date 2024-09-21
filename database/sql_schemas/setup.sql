CREATE DATABASE IF NOT EXISTS jolly_chimp;
USE jolly_chimp;

-- Create the user with caching_sha2_password
CREATE USER IF NOT EXISTS '${MYSQL_USER}'@'%' IDENTIFIED WITH caching_sha2_password BY '${MYSQL_PASSWORD}';

-- Grant privileges to the user on the database
GRANT ALL PRIVILEGES ON jolly_chimp.* TO '${MYSQL_USER}'@'%';

-- Flush privileges to ensure that the changes take effect
FLUSH PRIVILEGES;
