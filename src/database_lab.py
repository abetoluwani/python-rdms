import sqlite3

# This would Connect to SQLite database
database_name = "coffee_shop_database.db"
connection = sqlite3.connect(database_name)
print(f"Connected to database: {database_name}")

# We have to create a cursor object to execute SQL commands
cursor = connection.cursor()

# Function to check if a table exists
def table_exists(table_name):
    query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'"
    cursor.execute(query)
    return cursor.fetchone() is not None

# Create tables
table_creation_queries = [
    {
        "table_name": "Customers",
        "query": """
            CREATE TABLE IF NOT EXISTS Customers (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                email TEXT UNIQUE,
                phone_number TEXT,
                loyalty_points INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """
    },
    {
        "table_name": "Employees",
        "query": """
            CREATE TABLE IF NOT EXISTS Employees (
                employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                position TEXT,
                hire_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                salary REAL,
                email TEXT UNIQUE,
                phone_number TEXT
            );
        """
    },
    {
        "table_name": "Products",
        "query": """
            CREATE TABLE IF NOT EXISTS Products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                price REAL,
                category TEXT,
                is_available INTEGER DEFAULT 1
            );
        """
    },
    {
        "table_name": "Orders",
        "query": """
            CREATE TABLE IF NOT EXISTS Orders (
                order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER,
                order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                total_amount REAL,
                status TEXT,
                FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
            );
        """
    },
    {
        "table_name": "Order_Items",
        "query": """
            CREATE TABLE IF NOT EXISTS Order_Items (
                order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id INTEGER,
                product_id INTEGER,
                quantity INTEGER,
                price REAL,
                FOREIGN KEY (order_id) REFERENCES Orders(order_id),
                FOREIGN KEY (product_id) REFERENCES Products(product_id)
            );
        """
    },
    {
        "table_name": "Inventory",
        "query": """
            CREATE TABLE IF NOT EXISTS Inventory (
                inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT,
                quantity INTEGER,
                unit TEXT,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """
    },
    {
        "table_name": "Payments",
        "query": """
            CREATE TABLE IF NOT EXISTS Payments (
                payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id INTEGER,
                payment_method TEXT,
                payment_amount REAL,
                payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (order_id) REFERENCES Orders(order_id)
            );
        """
    },
    {
        "table_name": "Reviews",
        "query": """
            CREATE TABLE IF NOT EXISTS Reviews (
                review_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER,
                product_id INTEGER,
                rating INTEGER,
                review_text TEXT,
                review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
                FOREIGN KEY (product_id) REFERENCES Products(product_id)
            );
        """
    },
    {
        "table_name": "Shift_Schedules",
        "query": """
            CREATE TABLE IF NOT EXISTS Shift_Schedules (
                schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
                employee_id INTEGER,
                shift_start TIMESTAMP,
                shift_end TIMESTAMP,
                FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
            );
        """
    },
    {
        "table_name": "Promotions",
        "query": """
            CREATE TABLE IF NOT EXISTS Promotions (
                promotion_id INTEGER PRIMARY KEY AUTOINCREMENT,
                promotion_name TEXT,
                discount_percentage REAL,
                start_date TIMESTAMP,
                end_date TIMESTAMP,
                description TEXT
            );
        """
    },
    {
        "table_name": "Product_Promotions",
        "query": """
            CREATE TABLE IF NOT EXISTS Product_Promotions (
                product_id INTEGER,
                promotion_id INTEGER,
                PRIMARY KEY (product_id, promotion_id),
                FOREIGN KEY (product_id) REFERENCES Products(product_id),
                FOREIGN KEY (promotion_id) REFERENCES Promotions(promotion_id)
            );
        """
    },
]

# A for loop to loop through the table creation queries and create the tables
for table in table_creation_queries:
    if not table_exists(table["table_name"]):
        cursor.execute(table["query"])
        print(f"Table '{table['table_name']}' created.")
    else:
        print(f"Table '{table['table_name']}' already exists.")

# Close the connection
connection.close()
print("Database connection closed.")