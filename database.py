import sqlite3
# import os

def create_database():
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            phone TEXT,
            uni TEXT,
            stunum TEXT,
            email TEXT,
            want_license TEXT,
            relation TEXT
        )
    """)

    conn.commit()
    conn.close()

def insert_user_data(id, user_data):
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()

    # Insert data for a specific ID
    cursor.execute("""
        INSERT INTO users (id, name, age, phone, uni, stunum, email, want_license, relation)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (id,) + user_data)

    conn.commit()
    conn.close()

def update_user_data(id, element, value):
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()

    # Update the email for the specified user ID
    cursor.execute(f"UPDATE users SET {element} = ? WHERE id = ?", (value, id))

    conn.commit()
    conn.close()

def get_user_info_by_id(id, requested_fields):
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()

    # Construct the SQL query dynamically based on requested fields
    query = f"SELECT {', '.join(requested_fields)} FROM users WHERE id = ?"
    cursor.execute(query, (id,))
    user_info = cursor.fetchone()

    conn.close()
    return user_info

def get_element(id, element):
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()

    # Execute a query to retrieve the email for the specified user ID
    cursor.execute(f"SELECT {element} FROM users WHERE id = ?", (id,))
    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]  # Return the email address
    else:
        return None  # User not found
    
def delete_user_by_id(id):
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()

    # Delete the user with the specified ID
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))

    conn.commit()
    conn.close()

def check_user_exists(id):
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()

    # Execute a query to check if the user with the specified ID exists
    cursor.execute("SELECT 1 FROM users WHERE id = ?", (id,))
    result = cursor.fetchone()

    conn.close()

    return result is not None


# # Example usage:

# create_database()

# # Suppose you receive data for ID 1:
# user_data_1 = ("John Doe", 25, "123-456-7890", "Example University", "12345", "john@example.com", 1, "Friend")
# insert_user_data(1, user_data_1)

# # Later, data for ID 2:
# user_data_2 = ("Jane Smith", 30, "987-654-3210", "Another University", "54321", "jane@example.com", 0, "Colleague")
# insert_user_data(2, user_data_2)

# # Example usage:
# user_id = 1
# fields_to_retrieve = ['name', 'age', 'phone', 'uni', 'stunum', 'email', 'want_license', 'relation']
# user_info = get_user_info_by_id(user_id, fields_to_retrieve)


# # Example usage:
# user_id_to_update = 1
# new_email_address = "new.email@example.com"
# update_user_data(user_id_to_update, new_email_address)


# create_database()
# insert_user_data(1, ('mato','','','','','','',''))
# update_user_data(1, "email", "iran")

# print(check_user_exists(10))