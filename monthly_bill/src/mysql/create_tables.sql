-- Tabela de contas (bill)
CREATE TABLE bill (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    estimated_value INT NOT NULL,
    initial_mounth INT NOT NULL,
    final_mounth INT NOT NULL
);

-- Tabela de meses (mounth)
CREATE TABLE mounth (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

-- Tabela de instâncias de contas (bill_instance)
CREATE TABLE bill_instance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mounth_id INT NOT NULL,
    bill_id INT NOT NULL,
    paid BOOLEAN NOT NULL DEFAULT FALSE,
    real_value INT NULL,
    paid_date DATE NULL,
    FOREIGN KEY (mounth_id) REFERENCES mounth(id),
    FOREIGN KEY (bill_id) REFERENCES bill(id)
);
