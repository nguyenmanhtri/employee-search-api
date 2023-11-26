CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    telephone TEXT NULL,
    department TEXT NULL,
    position TEXT NULL,
    `location` TEXT NULL,
    `status` TEXT NOT NULL,
    company TEXT NULL
);

INSERT INTO employees (first_name, last_name, email, telephone, department, position, `location`, `status`, company) VALUES ('John', 'Doe', 'john.doe@example.com', NULL, 'IT', 'Developer', 'New York', 'Active', 'Company A');
INSERT INTO employees (first_name, last_name, email, telephone, department, position, `location`, `status`, company) VALUES ('Jane', 'Smith', 'jane.smith@example.com', '123-456-7890', 'Marketing', 'Analyst', 'San Francisco', 'Not started', 'Company B');
INSERT INTO employees (first_name, last_name, email, telephone, department, position, `location`, `status`, company) VALUES ('Emily', 'Johnson', 'emily.johnson@example.com', NULL, 'HR', 'Manager', 'Boston', 'Active', NULL);
INSERT INTO employees (first_name, last_name, email, telephone, department, position, `location`, `status`, company) VALUES ('Michael', 'Brown', 'michael.brown@example.com', '123-456-7891', NULL, 'Consultant', 'Chicago', 'Terminated', 'Company C');
INSERT INTO employees (first_name, last_name, email, telephone, department, position, `location`, `status`, company) VALUES ('Jessica', 'Davis', 'jessica.davis@example.com', NULL, 'Sales', 'Representative', 'Los Angeles', 'Active', 'Company D');
INSERT INTO employees (first_name, last_name, email, telephone, department, position, `location`, `status`, company) VALUES ('William', 'Miller', 'william.miller@example.com', '123-456-7892', 'IT', 'Developer', 'Austin', 'Not started', NULL);
INSERT INTO employees (first_name, last_name, email, telephone, department, position, `location`, `status`, company) VALUES ('Sarah', 'Wilson', 'sarah.wilson@example.com', NULL, 'Marketing', 'Analyst', 'Miami', 'Active', 'Company E');
INSERT INTO employees (first_name, last_name, email, telephone, department, position, `location`, `status`, company) VALUES ('James', 'Moore', 'james.moore@example.com', '123-456-7893', 'HR', 'Manager', 'Seattle', 'Terminated', NULL);
INSERT INTO employees (first_name, last_name, email, telephone, department, position, `location`, `status`, company) VALUES ('Elizabeth', 'Taylor', 'elizabeth.taylor@example.com', NULL, 'Sales', 'Representative', 'Denver', 'Active', 'Company F');
INSERT INTO employees (first_name, last_name, email, telephone, department, position, `location`, `status`, company) VALUES ('David', 'Anderson', 'david.anderson@example.com', '123-456-7894', 'IT', 'Developer', 'Atlanta', 'Not started', 'Company G');
INSERT INTO employees (first_name, last_name, email, telephone, department, position, `location`, `status`, company) VALUES ('Maria', 'Garcia', 'maria.garcia@example.com', NULL, 'Marketing', 'Analyst', 'Dallas', 'Active', NULL);
INSERT INTO employees (first_name, last_name, email, telephone, department, position, `location`, `status`, company) VALUES ('Robert', 'Hernandez', 'robert.hernandez@example.com', '123-456-7895', 'HR', 'Manager', 'Philadelphia', 'Terminated', 'Company H');
INSERT INTO employees (first_name, last_name, email, telephone, department, position, `location`, `status`, company) VALUES ('Linda', 'Martinez', 'linda.martinez@example.com', NULL, 'Sales', 'Representative', 'Phoenix', 'Active', 'Company I');
INSERT INTO employees (first_name, last_name, email, telephone, department, position, `location`, `status`, company) VALUES ('Thomas', 'Jackson', 'thomas.jackson@example.com', '123-456-7896', 'IT', 'Developer', 'San Antonio', 'Not started', NULL);
INSERT INTO employees (first_name, last_name, email, telephone, department, position, `location`, `status`, company) VALUES ('Patricia', 'Lee', 'patricia.lee@example.com', NULL, 'Marketing', 'Analyst', 'San Diego', 'Active', 'Company J');
