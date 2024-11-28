import sqlite3  # Ensure sqlite3 is imported

def add_member(name, email):
    with sqlite3.connect("library.db") as conn:
        cursor = conn.cursor()
        try:
            # Check if the email already exists
            cursor.execute("SELECT id FROM Members WHERE email = ?", (email,))
            if cursor.fetchone():
                return False, f"Error: A member with the email '{email}' is already registered."
            # Insert new member
            cursor.execute("INSERT INTO Members (name, email) VALUES (?, ?)", (name, email))
            conn.commit()
            return True, "Member registered successfully!"
        except sqlite3.Error as e:
            return False, f"Database error: {str(e)}"



def list_members():
    with sqlite3.connect("library.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Members")
        return cursor.fetchall()
