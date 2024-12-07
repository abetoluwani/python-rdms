import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
database_name = "lab6_database.db"
connection = sqlite3.connect(database_name)
print(f"Connected to database: {database_name}")

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

#   Create a sample table
table_creation_query = """
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    major TEXT NOT NULL
);
"""
cursor.execute(table_creation_query)
print("Table 'students' created (if it did not exist).")

# Insert sample data into the table
insert_query = """
INSERT INTO students (name, age, major)
VALUES
    ('Alice', 21, 'Computer Science'),
    ('Bob', 22, 'Mathematics'),
    ('Charlie', 20, 'Physics');
"""
cursor.execute(insert_query)
connection.commit()
print("Sample data inserted into 'students' table.")

# Query the data
select_query = "SELECT * FROM students;"
cursor.execute(select_query)
rows = cursor.fetchall()
print("Data in 'students' table:")
for row in rows:
    print(row)

# Update a record
update_query = "UPDATE students SET major = 'Engineering' WHERE name = 'Charlie';"
cursor.execute(update_query)
connection.commit()
print("Updated 'Charlie'\'s major to 'Engineering'.")

# Query the updated data
cursor.execute(select_query)
rows = cursor.fetchall()
print("Updated data in 'students' table:")
for row in rows:
    print(row)

# Close the connection
connection.close()
print("Database connection closed.")
