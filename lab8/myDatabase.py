import sqlite3

# Open database connection
conn = sqlite3.connect('contacts.db')
print("Opened database successfully")

# Create a table 
def create_Table():
    conn.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 NAME TEXT    NOT NULL,
                 PHONE TEXT NOT NULL);''')
    print("Table created successfully")


# Insert a record into the table
def insert_table(name, phone):
    conn.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", (name, phone))
    conn.commit()
    print("Record inserted successfully")

# Update a record in the table
def update_table(name, phone, contact_id):
    conn.execute("UPDATE contacts SET NAME = ?, PHONE = ? WHERE ID = ?", (name, phone, contact_id))
    conn.commit()
    print("Record updated successfully")

# Delete a record from the table
def delete_table(contact_id):
    conn.execute("DELETE FROM contacts WHERE ID = ?", (contact_id,))
    conn.commit()
    print("Record deleted successfully")

# Read all records from the table
def read_Contacts():
    cursor = conn.execute("SELECT NAME, PHONE FROM contacts")
    records = cursor.fetchall()
    print("Records fetched successfully")
    return records

def insert_contacts_from_list(contact_list):
    for contact in contact_list:
        name, phone = contact
        insert_table(name, phone)
    print("Contacts inserted from the list successfully")

create_Table()

