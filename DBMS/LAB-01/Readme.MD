
# Bank Database Schema

## QUES-01: Consider the following schema for bank database:
BRANCH(Branch_id , Bank_name,Branch_name , Assets)  

ACCOUNT(Acc_no,Branch_id,Account_type,Account_balance,Customer_id)  

CUSTOMER (Customer_id,Customer_name,Customer_age,Customer_address,Customer_phone)  

LOAN(Loan_number,Branch_id,Amount,Customer_id)  


---

## 🏦 Schema Details

### 1. BRANCH
Stores information about the different bank branches.

| Column       | Data Type | Constraints | Description |
|--------------|-----------|-------------|-------------|
| Branch_id    | INT       | PRIMARY KEY | Unique identifier for each branch |
| Bank_name    | VARCHAR   | NOT NULL    | Name of the bank |
| Branch_name  | VARCHAR   | NOT NULL    | Name of the branch |
| Assets       | DECIMAL   |             | Total assets of the branch |

---

### 2. ACCOUNT
Contains details about customer accounts.

| Column          | Data Type | Constraints | Description |
|-----------------|-----------|-------------|-------------|
| Acc_no          | INT       | PRIMARY KEY | Unique account number |
| Branch_id       | INT       | FOREIGN KEY | References **BRANCH(Branch_id)** |
| Account_type    | VARCHAR   | NOT NULL    | Type of account (e.g., Savings, Current) |
| Account_balance | DECIMAL   |             | Current balance in the account |
| Customer_id     | INT       | FOREIGN KEY | References **CUSTOMER(Customer_id)** |

---

### 3. CUSTOMER
Stores customer details.

| Column           | Data Type | Constraints | Description |
|------------------|-----------|-------------|-------------|
| Customer_id      | INT       | PRIMARY KEY | Unique identifier for each customer |
| Customer_name    | VARCHAR   | NOT NULL    | Full name of the customer |
| Customer_age     | INT       |             | Age of the customer |
| Customer_address | VARCHAR   |             | Address of the customer |
| Customer_phone   | VARCHAR   |             | Contact number of the customer |

---

### 4. LOAN
Keeps track of loans issued to customers.

| Column      | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| Loan_number | INT       | PRIMARY KEY | Unique identifier for each loan |
| Branch_id   | INT       | FOREIGN KEY | References **BRANCH(Branch_id)** |
| Amount      | DECIMAL   |             | Loan amount sanctioned |
| Customer_id | INT       | FOREIGN KEY | References **CUSTOMER(Customer_id)** |

---

## 🔗 Relationships
- **BRANCH ↔ ACCOUNT**: One branch can have multiple accounts.  
- **CUSTOMER ↔ ACCOUNT**: One customer can hold multiple accounts.  
- **CUSTOMER ↔ LOAN**: One customer can take multiple loans.  
- **BRANCH ↔ LOAN**: One branch can issue multiple loans.  

---

