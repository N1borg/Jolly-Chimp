CREATE TABLE IF NOT EXISTS websites (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL,
    ip VARCHAR(255),
    status BOOLEAN NOT NULL,
    latency INT
);
