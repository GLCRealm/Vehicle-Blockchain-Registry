
# Blockchain-Based Vehicle Registration System

A **Python-based blockchain application** designed to securely manage vehicle registration data. This system ensures data integrity, transparency, and security using blockchain principles such as cryptographic hashing and block linking.

---

## Features

### Blockchain Functionality:
- **Genesis Block**: A pre-defined root block for the blockchain.
- **Dynamic Block Addition**: Add new vehicle registration data as blocks.
- **Hash Integrity**: Each block is cryptographically secured with SHA-256.

### User-Friendly Operations:
1. **Add Registration**: Register a vehicle and store its data securely.
2. **View Data**:
   - Print all stored blocks.
   - Search specific blocks using a unique ID (`U_ID`).
3. **Menu-Driven Interface**: Interactive prompts for easy navigation.

### Security and Integrity:
- Unique IDs are generated using Python's `secrets` module.
- Immutability of blocks ensures tamper-proof records.
- Data is validated during input and storage.

---

## Setup and Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/blockchain-vehicle-registry.git
   cd blockchain-vehicle-registry
   ```

2. **Install Dependencies:**
   This script uses only standard Python libraries, but ensure you have Python 3.6+ installed.

3. **Run the Application:**
   ```bash
   python blockchain_backend.py
   ```

---

## Usage

### Menu Options:
1. **Add a New Registration:**
   - Input customer details such as name, vehicle number, dealership details, and dates (e.g., date of purchase).
   - The system generates a unique ID (`U_ID`) for every block.
   - Data is hashed and stored securely.

2. **Print Data:**
   - View all stored data or search for a specific block using `U_ID`.

3. **Exit:**
   - End the application session.

---

## Example Workflow

1. Start the application:
   ```text
   1.Add a new Registration
   2.Print Data
   3.EXIT
   ```

2. Add a new registration:
   ```text
   Enter the name of customer: John Doe
   Enter the vehicle number: ABC1234
   Enter the detail of dealership: XYZ Motors
   Enter the date of purchase (DD-MM-YYYY): 15-11-2023
   Enter the licence number of customer: LIC-56789
   Enter the date of birth of the customer (DD-MM-YYYY): 01-01-1990
   Enter the date of registration (DD-MM-YYYY): 16-11-2023
   Enter the address of the customer: 123 Main Street, CityName
   ```

   Output:
   ```text
   YOUR DATA IS UPLOADED
   Your Unique ID is: a1b2c3d4e5
   ```

3. Search for a specific registration:
   ```text
   Enter your unique ID: a1b2c3d4e5
   ```

   Output:
   ```text
   UNIQUE ID: a1b2c3d4e5
   NAME: John Doe
   VEHICLE NUMBER: ABC1234
   DETAIL OF DEALERSHIP: XYZ Motors
   DATE OF PURCHASE: 2023-11-15
   LICENCE NUMBER: LIC-56789
   DATE OF BIRTH: 1990-01-01
   DATE OF REGISTRATION: 2023-11-16
   ADDRESS: 123 Main Street, CityName
   ```

---

## Code Highlights

### Genesis Block:
The initial block (`create_first_block`) is a placeholder with no user data:
```python
def create_first_block():
    format = '%d/%m/%Y'
    b = datetime.datetime.strptime('11/11/1111', format)
    return block(0, 0, "NULL", "this is an empty block", "NULL", "NULL", b, "NULL", b, b, "NULL", calculate_hash(0, 0, "NULL", "NULL", "NULL", "NULL", b, "NULL", b, b, "NULL"))
```

### Hash Calculation:
Ensures data integrity using SHA-256:
```python
def calculate_hash(U_ID, index, previous_hash, data_name, data_car_number, data_DS_detail, data_DOP, data_licence_no, data_DOB, data_DOR, data_add):
    value = (
        f"{U_ID}{index}{previous_hash}{data_name}{data_car_number}{data_DS_detail}"
        f"{data_DOP.strftime('%d-%m-%Y')}{data_licence_no}{data_DOB.strftime('%d-%m-%Y')}"
        f"{data_DOR.strftime('%d-%m-%Y')}{data_add}"
    )
    return hashlib.sha256(value.encode()).hexdigest()
```

### Blockchain Validation:
(Optional) Implement a function to validate blockchain integrity:
```python
def validate_chain(blockchain):
    for i in range(1, len(blockchain)):
        current = blockchain[i]
        previous = blockchain[i-1]
        if current.previous_hash != previous.current_hash:
            return False
        if current.current_hash != calculate_hash(
                current.U_ID, current.index, current.previous_hash, current.data_name,
                current.data_car_number, current.data_DS_detail, current.data_DOP,
                current.data_licence_no, current.data_DOB, current.data_DOR, current.data_add):
            return False
    return True
```

---

## Planned Enhancements
- **Blockchain Validation:** Add a function to verify the entire blockchain.
- **Improved Security:** Encrypt sensitive fields like addresses and license numbers.
- **Scalability:** Use a database or file-based storage instead of in-memory lists.
- **Web Interface:** Build a simple front-end for user interaction.

---

## Contributing
Contributions are welcome! Please:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with detailed changes.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact
For questions or suggestions, feel free to reach out:
- **Author:** Hritvik Bhandri
- **Email:** [your-email@example.com]
- **LinkedIn:** [Your LinkedIn Profile](#)
