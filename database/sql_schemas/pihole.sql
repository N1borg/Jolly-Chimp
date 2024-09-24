CREATE TABLE IF NOT EXISTS pihole (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status BOOLEAN NOT NULL,
    dns_queries_today INT NOT NULL,
    ads_blocked_today INT NOT NULL,
    ads_percentage_today DECIMAL(5, 2) NOT NULL
);
