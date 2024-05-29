CREATE TABLE USERS (
    id INT NOT NULL IDENTITY(1, 1),
    username VARCHAR(64) NOT NULL,
    password_hash VARCHAR(200) NOT NULL,
    PRIMARY KEY (id)
);

-- password is 1234
INSERT INTO dbo.users (username, password_hash)
VALUES ('admin', 'scrypt:32768:8:1$daKsm0TmikhDvEhz$2b5081314ec2afa2a2e552605b6e592f96e495c866a9c248e1742292c5cea6b7325721c3250de56207f84ae602e92a714631fa08114bb8debc947d72538356e9');