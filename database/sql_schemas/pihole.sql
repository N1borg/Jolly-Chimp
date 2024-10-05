CREATE TABLE IF NOT EXISTS pihole (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    ip VARCHAR(255) NOT NULL,
    status BOOLEAN NOT NULL,
    dns_queries_today INT NOT NULL,
    ads_blocked_today INT NOT NULL,
    ads_percentage_today DECIMAL(5, 2) NOT NULL
);
