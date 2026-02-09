DROP TABLE IF EXISTS bill_instance;
DROP TABLE IF EXISTS bill;
DROP TABLE IF EXISTS mounth;

-- Tabela de contas (bill)
CREATE TABLE bill (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    estimated_value INT NOT NULL,
    initial_date DATE NOT NULL,
    final_date DATE NOT NULL
);

-- Tabela de instâncias de contas (bill_instance)
CREATE TABLE bill_instance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bill_id INT NOT NULL,
    month_year DATE NOT NULL,
    paid BOOLEAN NOT NULL DEFAULT FALSE,
    real_value INT NULL,
    paid_date DATE NULL,
    FOREIGN KEY (bill_id) REFERENCES bill(id) ON DELETE CASCADE
);
